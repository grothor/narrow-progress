#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

from data.video_games import *
import re

# Machinery for importing both copy-and-pasted and (where necessary) OCR'd tables from various Atari research papers
# Copying and pasting tables from PDFs produces very weird results sometimes, so we make no promises that there aren't
# any forms of weirdness here.

# The common case is that PDF tables paste column-wise; but some are row-wise so we have machinery for both.

# COLUMN-WISE RESULT TABLES:

wang_table_2 = """GAMES
Alien
Amidar
Assault
Asterix
Asteroids
Atlantis
Bank Heist
Battle Zone
Beam Rider
Berzerk
Bowling
Boxing
Breakout
Centipede
Chopper Command
Crazy Climber
Defender
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
H.E.R.O.
Ice Hockey
James Bond
Kangaroo
Krull
Kung-Fu Master
Montezuma’s Revenge
Ms. Pac-Man
Name This Game
Phoenix
Pitfall!
Pong
Private Eye
Q*Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Surround
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard Of Wor
Yars Revenge
Zaxxon
NO. ACTIONS
18
10
7
9
14
4
18
18
9
18
6
18
4
18
18
9
18
6
18
9
18
3
18
8
18
18
18
18
18
18
14
18
9
6
8
18
3
18
6
18
18
18
18
3
18
6
18
5
18
10
8
6
18
9
10
18
18
R ANDOM
227.8
5.8
222.4
210.0
719.1
12,850.0
14.2
2,360.0
363.9
123.7
23.1
0.1
1.7
2,090.9
811.0
10,780.5
2,874.5
152.1
-18.6
0.0
-91.7
0.0
65.2
257.6
173.0
1,027.0
-11.2
29.0
52.0
1,598.0
258.5
0.0
307.3
2,292.3
761.4
-229.4
-20.7
24.9
163.9
1,338.5
11.5
2.2
68.4
-17,098.1
1,236.3
148.0
664.0
-10.0
-23.8
3,568.0
11.4
533.4
0.0
16,256.9
563.5
3,092.9
32.5
HUMAN
7,127.7
1,719.5
742.0
8,503.3
47,388.7
29,028.1
753.1
37,187.5
16,926.5
2,630.4
160.7
12.1
30.5
12,017.0
7,387.8
35,829.4
18,688.9
1,971.0
-16.4
860.5
-38.7
29.6
4,334.7
2,412.5
3,351.4
30,826.4
0.9
302.8
3,035.0
2,665.5
22,736.3
4,753.3
6,951.6
8,049.0
7,242.6
6,463.7
14.6
69,571.3
13,455.0
17,118.0
7,845.0
11.9
42,054.7
-4,336.9
12,326.7
1,668.7
10,250.0
6.5
-8.3
5,229.2
167.6
11,693.2
1,187.5
17,667.9
4,756.5
54,576.9
9,173.3
DQN
1,620.0
978.0
4,280.4
4,359.0
1,364.5
279,987.0
455.0
29,900.0
8,627.5
585.6
50.4
88.0
385.5
4,657.7
6,126.0
110,763.0
23,633.0
12,149.4
-6.6
729.0
-4.9
30.8
797.4
8,777.4
473.0
20,437.8
-1.9
768.5
7,259.0
8,422.3
26,059.0
0.0
3,085.6
8,207.8
8,485.2
-286.1
19.5
146.7
13,117.3
7,377.6
39,544.0
63.9
5,860.6
-13,062.3
3,482.8
1,692.3
54,282.0
-5.6
12.2
4,870.0
68.1
9,989.9
163.0
196,760.4
2,704.0
18,098.9
5,363.0
DDQN
3,747.7
1,793.3
5,393.2
17,356.5
734.7
106,056.0
1,030.6
31,700.0
13,772.8
1,225.4
68.1
91.6
418.5
5,409.4
5,809.0
117,282.0
35,338.5
58,044.2
-5.5
1,211.8
15.5
33.3
1,683.3
14,840.8
412.0
20,130.2
-2.7
1,358.0
12,992.0
7,920.5
29,710.0
0.0
2,711.4
10,616.0
12,252.5
-29.9
20.9
129.7
15,088.5
14,884.5
44,127.0
65.1
16,452.7
-9,021.8
3,067.8
2,525.5
60,142.0
-2.9
-22.8
8,339.0
218.4
22,972.2
98.0
309,941.9
7,492.0
11,712.6
10,163.0
DUEL
4,461.4
2,354.5
4,621.0
28,188.0
2,837.7
382,572.0
1,611.9
37,150.0
12,164.0
1,472.6
65.5
99.4
345.3
7,561.4
11,215.0
143,570.0
42,214.0
60,813.3
0.1
2,258.2
46.4
0.0
4,672.8
15,718.4
588.0
20,818.2
0.5
1,312.5
14,854.0
11,451.9
34,294.0
0.0
6,283.5
11,971.1
23,092.2
0.0
21.0
103.0
19,220.3
21,162.6
69,524.0
65.3
50,254.2
-8,857.4
2,250.8
6,427.3
89,238.0
4.4
5.1
11,666.0
211.4
44,939.6
497.0
98,209.5
7,855.0
49,622.1
12,944.0
P RIOR .
4,203.8
1,838.9
7,672.1
31,527.0
2,654.3
357,324.0
1,054.6
31,530.0
23,384.2
1,305.6
47.9
95.6
373.9
4,463.2
8,600.0
141,161.0
31,286.5
71,846.4
18.5
2,093.0
39.5
33.7
4,380.1
32,487.2
548.5
23,037.7
1.3
5,148.0
16,200.0
9,728.0
39,581.0
0.0
6,518.7
12,270.5
18,992.7
-356.5
20.6
200.0
16,256.5
14,522.3
57,608.0
62.6
26,357.8
-9,996.9
4,309.0
2,865.8
63,302.0
8.9
0.0
9,197.0
204.6
16,154.1
54.0
282,007.3
4,802.0
11,357.0
10,469.0
PRIOR. DUEL.
3,941.0
2,296.8
11,477.0
375,080.0
1,192.7
395,762.0
1,503.1
35,520.0
30,276.5
3,409.0
46.7
98.9
366.0
7,687.5
13,185.0
162,224.0
41,324.5
72,878.6
-12.5
2,306.4
41.3
33.0
7,413.0
104,368.2
238.0
21,036.5
-0.4
812.0
1,792.0
10,374.4
48,375.0
0.0
3,327.3
15,572.5
70,324.3
0.0
20.9
206.0
18,760.3
20,607.6
62,151.0
27.5
931.6
-19,949.9
133.4
15,311.5
125,117.0
1.2
0.0
7,553.0
245.9
33,879.1
48.0
479,197.0
12,352.0
69,618.1
13,886.0"""

wang_table_3 = """GAMES
Alien
Amidar
Assault
Asterix
Asteroids
Atlantis
Bank Heist
Battle Zone
Beam Rider
Berzerk
Bowling
Boxing
Breakout
Centipede
Chopper Command
Crazy Climber
Defender
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
H.E.R.O.
Ice Hockey
James Bond
Kangaroo
Krull
Kung-Fu Master
Montezuma’s Revenge
Ms. Pac-Man
Name This Game
Phoenix
Pitfall!
Pong
Private Eye
Q*Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Surround
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard Of Wor
Yars Revenge
Zaxxon
N O . A CTIONS
18
10
7
9
14
4
18
18
9
18
6
18
4
18
18
9
18
6
18
9
18
3
18
8
18
18
18
18
18
18
14
18
9
6
8
18
3
18
6
18
18
18
18
3
18
6
18
5
18
10
8
6
18
9
10
18
18
R ANDOM
128.3
11.8
166.9
164.5
871.3
13,463.0
21.7
3,560.0
254.6
196.1
35.2
-1.5
1.6
1,925.5
644.0
9,337.0
1,965.5
208.3
-16.0
-81.8
-77.1
0.1
66.4
250.0
245.5
1,580.3
-9.7
33.5
100.0
1,151.9
304.0
25.0
197.8
1,747.8
1,134.4
-348.8
-18.0
662.8
183.0
588.3
200.0
2.4
215.5
-15,287.4
2,047.2
182.6
697.0
-9.7
-21.4
3,273.0
12.7
707.2
18.0
20,452.0
804.0
1,476.9
475.0
HUMAN
6,371.3
1,540.4
628.9
7,536.0
36,517.3
26,575.0
644.5
33,030.0
14,961.0
2,237.5
146.5
9.6
27.9
10,321.9
8,930.0
32,667.0
14,296.0
3,442.8
-14.4
740.2
5.1
25.6
4,202.8
2,311.0
3,116.0
25,839.4
0.5
368.5
2,739.0
2,109.1
20,786.8
4,182.0
15,375.0
6,796.0
6,686.2
5,998.9
15.5
64,169.1
12,085.0
14,382.2
6,878.0
8.9
40,425.8
-3,686.6
11,032.6
1,464.9
9,528.0
5.4
-6.7
5,650.0
138.3
9,896.1
1,039.0
15,641.1
4,556.0
47,135.2
8,443.0
DQN
634.0
178.4
3,489.3
3,170.5
1,458.7
292,491.0
312.7
23,750.0
9,743.2
493.4
56.5
70.3
354.5
3,973.9
5,017.0
98,128.0
15,917.5
12,550.7
-6.0
626.7
-1.6
26.9
496.1
8,190.4
298.0
14,992.9
-1.6
697.5
4,496.0
6,206.0
20,882.0
47.0
1,092.3
6,738.8
7,484.8
-113.2
18.0
207.9
9,271.5
4,748.5
35,215.0
58.7
4,216.7
-12,142.1
1,295.4
1,293.8
52,970.0
-6.0
11.1
4,786.0
45.6
8,038.5
136.0
154,414.1
1,609.0
4,577.5
4,412.0
DDQN
1,033.4
169.1
6,060.8
16,837.0
1,193.2
319,688.0
886.0
24,740.0
17,417.2
1,011.1
69.6
73.5
368.9
3,853.5
3,495.0
113,782.0
27,510.0
69,803.4
-0.3
1,216.6
3.2
28.8
1,448.1
15,253.0
200.5
14,892.5
-2.5
573.0
11,204.0
6,796.1
30,207.0
42.0
1,241.3
8,960.3
12,366.5
-186.7
19.1
-575.5
11,020.8
10,838.4
43,156.0
59.1
14,498.0
-11,490.4
810.0
2,628.7
58,365.0
1.9
-7.8
6,608.0
92.2
19,086.9
21.0
367,823.7
6,201.0
6,270.6
8,593.0
D UEL
1,486.5
172.7
3,994.8
15,840.0
2,035.4
445,360.0
1,129.3
31,320.0
14,591.3
910.6
65.7
77.3
411.6
4,881.0
3,784.0
124,566.0
33,996.0
56,322.8
-0.8
2,077.4
-4.1
0.2
2,332.4
20,051.4
297.0
15,207.9
-1.3
835.5
10,334.0
8,051.6
24,288.0
22.0
2,250.6
11,185.1
20,410.5
-46.9
18.8
292.6
14,175.8
16,569.4
58,549.0
62.0
37,361.6
-11,928.0
1,768.4
5,993.1
90,804.0
4.0
4.4
6,601.0
48.0
24,759.2
200.0
110,976.2
7,054.0
25,976.5
10,164.0
P RIOR .
1,334.7
129.1
6,548.9
22,484.5
1,745.1
330,647.0
876.6
25,520.0
31,181.3
865.9
52.0
72.3
343.0
3,489.1
4,635.0
127,512.0
23,666.5
61,277.5
16.0
1,831.0
9.8
28.9
3,510.0
34,858.8
269.5
20,889.9
-0.2
3,961.0
12,185.0
6,872.8
31,676.0
51.0
1,865.9
10,497.6
16,903.6
-427.0
18.9
670.7
9,944.0
11,807.2
52,264.0
56.2
25,463.7
-10,169.1
2,272.8
3,912.1
61,582.0
5.9
-5.3
5,963.0
56.9
12,157.4
94.0
295,972.8
5,727.0
4,687.4
9,474.0
P RIOR . D UEL .
823.7
238.4
10,950.6
364,200.0
1,021.9
423,252.0
1,004.6
30,650.0
37,412.2
2,178.6
50.4
79.2
354.6
5,570.2
8,058.0
127,853.0
34,415.0
73,371.3
-10.7
2,223.9
17.0
28.2
4,038.4
105,148.4
167.0
15,459.2
0.5
585.0
861.0
7,658.6
37,484.0
24.0
1,007.8
13,637.9
63,597.0
-243.6
18.4
1,277.6
14,063.0
16,496.8
54,630.0
24.7
1,431.2
-18,955.8
280.6
8,978.0
127,073.0
-0.2
-13.2
4,871.0
108.6
22,681.3
29.0
447,408.6
10,471.0
58,145.9
11,320.0"""

# Absorb the data from https://arxiv.org/abs/1703.03864v1

# Copy and paste from Table 3:

es_table3 = """Game
Alien
Amidar
Assault
Asterix
Asteroids
Atlantis
Bank Heist
Battle Zone
Beam Rider
Berzerk
Bowling
Boxing
Breakout
Centipede
Chopper Command
Crazy Climber
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
Ice Hockey
Kangaroo
Krull
Montezumas Revenge
Name This Game
Phoenix
Pitfall!
Pong
Private Eye
Q Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard of Wor
Yars Revenge
Zaxxon
DQN
570.2
133.4
3332.3
124.5
697.1
76108.0
176.3
17560.0
8672.4
NaN
41.2
25.8
303.9
3773.1
3046.0
50992.0
12835.2
-21.6
475.6
-2.3
25.8
157.4
2731.8
216.5
-3.8
2696.0
3864.0
50.0
5439.9
NaN
NaN
16.2
298.2
4589.8
4065.3
9264.0
58.5
2793.9
NaN
NaN
1449.7
34081.0
-2.3
5640.0
32.4
3311.3
54.0
20228.1
246.0
NaN
831.0
A3C FF, 1 day
182.1
283.9
3746.1
6723.0
3009.4
772392.0
946.0
11340.0
13235.9
1433.4
36.2
33.7
551.6
3306.5
4669.0
101624.0
84997.5
0.1
-82.2
13.6
0.1
180.1
8442.8
269.5
-4.7
106.0
8066.6
53.0
5614.0
28181.8
-123.0
11.4
194.4
13752.3
10001.2
31769.0
2.3
2300.2
-13700.0
1884.8
2214.7
64393.0
-10.2
5825.0
26.1
54525.4
19.0
185852.6
5278.0
7270.8
2659.0
ES FF, 1 hour
994.0
112.0
1673.9
1440.0
1562.0
1267410.0
225.0
16600.0
744.0
686.0
30.0
49.8
9.5
7783.9
3710.0
26430.0
1166.5
0.2
95.0
-49.0
31.0
370.0
582.0
805.0
-4.1
11200.0
8647.2
0.0
4503.0
4041.0
0.0
21.0
100.0
147.5
5009.0
16590.0
11.9
1390.0
-15442.5
2090.0
678.5
1470.0
-4.5
4970.0
130.3
67974.0
760.0
22834.8
3480.0
16401.7
6380.0"""

bellemare_figure_14 = """GAMES
Alien
Amidar
Assault
Asterix
Asteroids
Atlantis
Bank Heist
Battle Zone
Beam Rider
Berzerk
Bowling
Boxing
Breakout
Centipede
Chopper Command
Crazy Climber
Defender
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
H.E.R.O.
Ice Hockey
James Bond
Kangaroo
Krull
Kung-Fu Master
Montezuma’s Revenge
Ms. Pac-Man
Name This Game
Phoenix
Pitfall!
Pong
Private Eye
Q*Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Surround
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard Of Wor
Yars’ Revenge
Zaxxon
RANDOM
227.8
5.8
222.4
210.0
719.1
12,850.0
14.2
2,360.0
363.9
123.7
23.1
0.1
1.7
2,090.9
811.0
10,780.5
2,874.5
152.1
-18.6
0.0
-91.7
0.0
65.2
257.6
173.0
1,027.0
-11.2
29.0
52.0
1,598.0
258.5
0.0
307.3
2,292.3
761.4
-229.4
-20.7
24.9
163.9
1,338.5
11.5
2.2
68.4
-17,098.1
1,236.3
148.0
664.0
-10.0
-23.8
3,568.0
11.4
533.4
0.0
16,256.9
563.5
3,092.9
32.5 
HUMAN
7,127.7
1,719.5
742.0
8,503.3
47,388.7
29,028.1
753.1
37,187.5
16,926.5
2,630.4
160.7
12.1
30.5
12,017.0
7,387.8
35,829.4
18,688.9
1,971.0
-16.4
860.5
-38.7
29.6
4,334.7
2,412.5
3,351.4
30,826.4
0.9
302.8
3,035.0
2,665.5
22,736.3
4,753.3
6,951.6
8,049.0
7,242.6
6,463.7
14.6
69,571.3
13,455.0
17,118.0
7,845.0
11.9
42,054.7
-4,336.9
12,326.7
1,668.7
10,250.0
6.5
-8.3
5,229.2
167.6
11,693.2
1,187.5
17,667.9
4,756.5
54,576.9
9,173.3
DQN
1,620.0
978.0
4,280.4
4,359.0
1,364.5
279,987.0
455.0
29,900.0
8,627.5
585.6
50.4
88.0
385.5
4,657.7
6,126.0
110,763.0
23,633.0
12,149.4
-6.6
729.0
-4.9
30.8
797.4
8,777.4
473.0
20,437.8
-1.9
768.5
7,259.0
8,422.3
26,059.0
0.0
3,085.6
8,207.8
8,485.2
-286.1
19.5
146.7
13,117.3
7,377.6
39,544.0
63.9
5,860.6
-13,062.3
3,482.8
1,692.3
54,282.0
-5.6
12.2
4,870.0
68.1
9,989.9
163.0
196,760.4
2,704.0
18,098.9
5,363.0
DDQN
3,747.7
1,793.3
5,393.2
17,356.5
734.7
106,056.0
1,030.6
31,700.0
13,772.8
1,225.4
68.1
91.6
418.5
5,409.4
5,809.0
117,282.0
35,338.5
58,044.2
-5.5
1,211.8
15.5
33.3
1,683.3
14,840.8
412.0
20,130.2
-2.7
1,358.0
12,992.0
7,920.5
29,710.0
0.0
2,711.4
10,616.0
12,252.5
-29.9
20.9
129.7
15,088.5
14,884.5
44,127.0
65.1
16,452.7
-9,021.8
3,067.8
2,525.5
60,142.0
-2.9
-22.8
8,339.0
218.4
22,972.2
98.0
309,941.9
7,492.0
11,712.6
10,163.0
DUEL
4,461.4
2,354.5
4,621.0
28,188.0
2,837.7
382,572.0
1,611.9
37,150.0
12,164.0
1,472.6
65.5
99.4
345.3
7,561.4
11,215.0
143,570.0
42,214.0
60,813.3
0.1
2,258.2
46.4
0.0
4,672.8
15,718.4
588.0
20,818.2
0.5
1,312.5
14,854.0
11,451.9
34,294.0
0.0
6,283.5
11,971.1
23,092.2
0.0
21.0
103.0
19,220.3
21,162.6
69,524.0
65.3
50,254.2
-8,857.4
2,250.8
6,427.3
89,238.0
4.4
5.1
11,666.0
211.4
44,939.6
497.0
98,209.5
7,855.0
49,622.1
12,944.0
PRIOR. DUEL.
3,941.0
2,296.8
11,477.0
375,080.0
1,192.7
395,762.0
1,503.1
35,520.0
30,276.5
3,409.0
46.7
98.9
366.0
7,687.5
13,185.0
162,224.0
41,324.5
72,878.6
-12.5
2,306.4
41.3
33.0
7,413.0
104,368.2
238.0
21,036.5
-0.4
812.0
1,792.0
10,374.4
48,375.0
0.0
3,327.3
15,572.5
70,324.3
0.0
20.9
206.0
18,760.3
20,607.6
62,151.0
27.5
931.6
-19,949.9
133.4
15,311.5
125,117.0
1.2
0.0
7,553.0
245.9
33,879.1
48.0
479,197.0
12,352.0
69,618.1
13,886.0
C51
3,166
1,735
7,203
406,211
1,516
841,075
976
28,742
14,074
1,645
81.8
97.8
748
9,646
15,600
179,877
47,092
130,955
2.5
3,454
8.9
33.9
3,965
33,641
440
38,874
-3.5
1,909
12,853
9,735
48,192
0.0
3,415
12,542
17,490
0.0
20.9
15,095
23,784
17,322
55,839
52.3
266,434
-13,901
8,342
5,747
49,095
6.8
23.1
8,329
280
15,612
1,520
949,604
9,300
35,050
10,513"""

mnih_2013_table_1 = """Random
Sarsa [3]
Contingency [4]
DQN
Human
HNeat Best [8]
HNeat Pixel [8]
DQN Best
B. Rider Breakout Enduro Pong Q*bert Seaquest S. Invaders
354
996
1743
4092
7456
3616
1332
5184
1.2
5.2
6
168
31
52
4
225
0
129
159
470
368
106
91
661
−20.4
−19
−17
20
−3
19
−16
21
157
614
960
1952
18900
1800
1325
4500
110
665
723
1705
28010
920
800
1740
179
271
268
581
3690
1720
1145
1075"""

van_hasselt_2016_table1 = """Game
Alien
Amidar
Assault
Asterix
Asteroids
Atlantis
Bank Heist
Battle Zone
Beam Rider
Berzerk
Bowling
Boxing
Breakout
Centipede
Chopper Command
Crazy Climber
Defender
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
H.E.R.O.
Ice Hockey
James Bond
Kangaroo
Krull
Kung-Fu Master
Montezuma’s Revenge
Ms. Pacman
Name This Game
Phoenix
Pitfall
Pong
Private Eye
Q*Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Surround
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard of Wor
Yars Revenge
Zaxxon
Random
227.80
5.80
222.40
210.00
719.10
12850.00
14.20
2360.00
363.90
123.70
23.10
0.10
1.70
2090.90
811.00
10780.50
2874.50
152.10
−18.60
0.00
−91.70
0.00
65.20
257.60
173.00
1027.00
−11.20
29.00
52.00
1598.00
258.50
0.00
307.30
2292.30
761.40
−229.40
−20.70
24.90
163.90
1338.50
11.50
2.20
68.40
−17098.10
1236.30
148.00
664.00
−10.00
−23.80
3568.00
11.40
533.40
0.00
16256.90
563.50
3092.90
32.50
Human
7127.70
1719.50
742.00
8503.30
47388.70
29028.10
753.10
37187.50
16926.50
2630.40
160.70
12.10
30.50
12017.00
7387.80
35829.40
18688.90
1971.00
−16.40
860.50
−38.70
29.60
4334.70
2412.50
3351.40
30826.40
0.90
302.80
3035.00
2665.50
22736.30
4753.30
6951.60
8049.00
7242.60
6463.70
14.60
69571.30
13455.00
17118.00
7845.00
11.90
42054.70
−4336.90
12326.70
1668.70
10250.00
6.50
−8.30
5229.20
167.60
11693.20
1187.50
17667.90
4756.50
54576.90
9173.30
Double DQN
3747.70
1793.30
5393.20
17356.50
734.70
106056.00
1030.60
31700.00
13772.80
1225.40
68.10
91.60
418.50
5409.40
5809.00
117282.00
35338.50
58044.20
−5.50
1211.80
15.50
33.30
1683.30
14840.80
412.00
20130.20
−2.70
1358.00
12992.00
7920.50
29710.00
0.00
2711.40
10616.00
12252.50
−29.90
20.90
129.70
15088.50
14884.50
44127.00
65.10
16452.70
−9021.80
3067.80
2525.50
60142.00
−2.90
−22.80
8339.00
218.40
22972.20
98.00
309941.90
7492.00
11712.60
10163.00
Double DQN with Pop-Art
3213.50
782.50
9011.60
18919.50
2869.30
340076.00
1103.30
8220.00
8299.40
1199.60
102.10
99.30
344.10
49065.80
775.00
119679.00
11099.00
63644.90
−11.50
2002.10
45.10
33.40
3469.60
56218.20
483.50
14225.20
−4.10
507.50
13150.00
9745.10
34393.00
0.00
4963.80
15851.20
6202.50
−2.60
20.60
286.70
5236.80
12530.80
47770.00
64.30
10932.30
−13585.10
4544.80
2589.70
589.00
−2.50
12.10
4870.00
183.90
22474.40
1172.00
56287.00
483.00
21409.50
14402.00"""

martin_table_1 = """Game
Venture
Montezuma's Revenge
Freeway
Frostbite
Q-bert
Sarsa-φ-EB
1169.2
2745.4
0.0
2770.1
4111.8
Sarsa-ε
0.0
399.5
29.9
1394.3
3895.3
DDQN-PC
N/A
3459
N/A
N/A
N/A
A3C+
0
142
27
507
15805
TRPO-Hash
445
75
34
5214
N/A
MP-EB
N/A
0
12
380
N/A
DDQN
98
0
33
1683
15088
DQN-PA
1172
0
33
3469
5237
Gorila
1245
4
12
605
10816
TRPO
121
0
16
2869
7733
Dueling
497
0
0
4672
19220"""


# COLUMN-ORIENTED processing

remove_re = re.compile(r"['’!\.]")
underscore_re = re.compile(r"[ \-\*]")
def game_metric_name(s):
    "Calculate the name of the Metric() object from a game's name"
    name = s.strip().lower()
    name = remove_re.sub("", name)
    name = underscore_re.sub("_", name)
    name = name.replace("pac_man", "pacman")  # the papers are inconsistent; "Pac-Man" is most correct but pacman most pythonic
    name = name.replace("pit_fall", "pitfall")  # "Pitfall!" not "Pit Fall"
    name = name.replace("jamesbond", "james_bond")  # "James Bond" not "Jamesbond"
    name = name.replace("montezuma_revenge", "montezumas_revenge")  # The variable has the s and no apostrophe
    name = name.replace("riverraid", "river_raid")  # "River Raid" not "Riverraid"
    name = name.replace("qbert", "q_bert")  # "Q*bert", I think, but the variable name is "q_bert_metric"
    name = name.replace("up_n_down", "up_and_down")  # "Up and Down" not "Up n Down"

    return name + "_metric"

verb = False # Set to True for debugging
TSIZE = 57   # Number of games reported in the more recent papers

def get_game_metric(metric_name, human_name, target, target_source):
    """Get a reference to the metric object for a game, creating it if necessary."""
    metric = globals().get(metric_name, None)
    if not metric:
        if verb: print("Creating metric for", human_name, "target: " + str(target) if target else "")
        metric = simple_games.metric("Atari 2600 " + human_name, target=target, 
                                     scale=atari_linear, target_source=target_source, atari=True)
        globals()[metric_name] = metric
    return metric

def get_column(raw, n, size=TSIZE):
    assert isinstance(raw, list), "Not a list: {0}".format(type(raw))
    start_pos = n * (size + 1) # Size + headers
    name = raw[start_pos]
    data = raw[start_pos + 1:start_pos + size + 1]
    return name, data

def ingest_column(src, n, paper_url, alg=None, extras={}, size=TSIZE):
    algorithm, data = get_column(src, n, size=size)
    _, games = get_column(src, 0, size=size)
    if verb and algorithm.lower() not in alg.lower():
        print(u"# {0} not in {1}".format(algorithm, alg))
    for i, score in enumerate(data):
        # Maybe someone should fix Python's float() function...
        if score.lower() == "n/a": continue
        score = float(score.replace(",", "").replace('\xe2\x88\x92', "-").replace("−", "-"))
        game = game_metric_name(games[i])
        metric = get_game_metric(game, games[i], targets[i], "https://arxiv.org/abs/1509.06461")
        if verb: print(u'{0}.measure(None, {1}, "{2}", url="{3}"{4})'.format(game, score, alg, paper_url, extras if extras else ""))
        metric.measure(None, score, alg, url=paper_url, **extras)


noop_data = wang_table_2.split("\n")
human_start_data = wang_table_3.split("\n")
es_data = es_table3.split("\n")
distributional_data = bellemare_figure_14.split("\n")
early_data = mnih_2013_table_1.split("\n")
pop_art_data = van_hasselt_2016_table1.split("\n")
sarsa_epsilon_data = martin_table_1.split("\n")

# Weirdly, the noop start human performance is consistently better than the human start human performance data
# Is this because it's newer and at a higher standard? Or because the recorded human starts consistently hamper strong
# human play?
_, human_noop = get_column(noop_data, 3)
human_noop = [float(score.replace(",", "")) for score in human_noop]
_, human_human = get_column(human_start_data, 3)
human_human = [float(score.replace(",", "")) for score in human_human]
targets = [max(scores) for scores in zip(human_noop, human_human)]

#ingest_column(early_data, 2, "https://arxiv.org/abs/1312.5602", u"SARSA(λ)", 
#              {"algorithm_src_url": "https://arxiv.org/abs/1207.4708v1"}, size=7)
ingest_column(es_data, 3, "https://arxiv.org/abs/1703.03864v1", "ES FF (1 hour) noop", size=51)
ingest_column(distributional_data, 7, "https://arxiv.org/abs/1707.06887v1", "C51 noop")
ingest_column(pop_art_data, 4, "https://arxiv.org/abs/1602.07714v1", "DDQN+Pop-Art noop")

ingest_column(noop_data, 4, "https://arxiv.org/abs/1509.06461v1", "DQN noop", 
              {"algorithm_src_url": "https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf",
               "min_date": date(2015, 2, 26)})
ingest_column(human_start_data, 4, "https://arxiv.org/abs/1509.06461v1", "DQN hs", 
              {"algorithm_src_url": "https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf",
               "min_date": date(2015, 2, 26)})

ingest_column(sarsa_epsilon_data, 1, "https://arxiv.org/abs/1706.08090", u"Sarsa-φ-EB",size=5)
ingest_column(sarsa_epsilon_data, 2, "https://arxiv.org/abs/1706.08090", u"Sarsa-ε", size=5)
ingest_column(sarsa_epsilon_data, 3, "https://arxiv.org/abs/1606.01868", "DDQN-PC", size=5)
ingest_column(sarsa_epsilon_data, 4, "https://arxiv.org/abs/1507.00814", "MP-EB", size=5)
ingest_column(sarsa_epsilon_data, 5, "https://arxiv.org/abs/1611.04717", "TRPO-hash", size=5)

# v1 of the DDQN paper reported only "untuned" results
# TODO import those "untuned" results. May require OCR due to missing table columns...

# v3 of that paper added "tuned" results for the hs condition

# However this (presumably tuned) DDQN noop data is included by Wang et al but seems NOT to be in the DDQN paper.
# Conjecture, did Wang et al first report it?
ingest_column(noop_data, 5, "https://arxiv.org/abs/1511.06581v1", "DDQN (tuned) noop",
              {"algorithm_src_url": "https://arxiv.org/abs/1509.06461v3"}) 

ingest_column(human_start_data, 5, "https://arxiv.org/abs/1509.06461v3", alg="DDQN (tuned) hs")
ingest_column(noop_data, 6, "https://arxiv.org/abs/1511.06581v1", alg="Duel noop")
ingest_column(human_start_data, 6, "https://arxiv.org/abs/1511.06581v1", alg="Duel hs")
ingest_column(noop_data, 7, "https://arxiv.org/abs/1511.05952", alg="Prior noop")
ingest_column(human_start_data, 7, "https://arxiv.org/abs/1511.05952", alg="Prior hs")
ingest_column(noop_data, 8, "https://arxiv.org/abs/1511.06581v3", "Prior+Duel noop", 
              {"algorithm_src_url":"https://arxiv.org/abs/1511.05952"})
ingest_column(human_start_data, 8, "https://arxiv.org/abs/1509.06461v3", "Prior+Duel hs", 
              {"algorithm_src_url":"https://arxiv.org/abs/1511.05952"})

# ROW-ORIENTED DATA

# The row parsers are harder and need to be customized per table, essentially

# OCR output:
mnih_extended_table_2 = """Game	Random Play	Best Linear Learner	Contingency (SARSA)	Human	DQN (± std)	Normalized DQN (% Human)
Alien	227.8	939.2	103.2	6875	3069 (±1093)	42.7%
Amidar	5.8	103.4	183.6	1676	739.5 (±3024)	43.9%
Assault	222.4	628	537	1496	3359 (±775)	246.2%
Asterix	210	987.3	1332	8503	6012 (±1744)	70.0%
Asteroids	719.1	907.3	89	13157	1629 (±542)	7.3%
Atlantis	12850	62687	852.9	29028	85641 (±17600)	449.9%
Bank Heist	14.2	190.8	67.4	734.4	429.7 (±650)	57.7%
Battle Zone	2360	15820	16.2	37800	26300 (±7725)	67.6%
Beam Rider	363.9	929.4	1743	5775	6846 (±1619)	119.8%
Bowling	23.1	43.9	36.4	154.8	42.4 (±88)	14.7%
Boxing	0.1	44	9.8	4.3	71.8 (±8.4)	1707.9%
Breakout	1.7	5.2	6.1	31.8	401.2 (±26.9)	1327.2%
Centipede	2091	8803	4647	11963	8309 (±5237)	63.0%
Chopper Command	811	1582	16.9	9882	6687 (±2916)	64.8%
Crazy Climber	10781	23411	149.8	35411	114103 (±22797)	419.5%
Demon Attack	152.1	520.5	0	3401	9711 (±2406)	294.2%
Double Dunk	-18.6	-13.1	-16	-15.5	-18.1 (±2.6)	17.1%
Enduro	0	129.1	159.4	309.6	301.8 (±24.6)	97.5%
Fishing Derby	-91.7	-89.5	-85.1	5.5	-0.8 (±19.0)	93.5%
Freeway	0	19.1	19.7	29.6	30.3 (±0.7)	102.4%
Frostbite	65.2	216.9	180.9	4335	328.3 (±250.5)	6.2%
Gopher	257.6	1288	2368	2321	8520 (±3279)	400.4%
Gravitar	173	387.7	429	2672	306.7 (±223.9)	5.3%
H.E.R.O.	1027	6459	7295	25763	19950 (±158)	76.5%
Ice Hockey	-11.2	-9.5	-3.2	0.9	-1.6 (±2.5)	79.3%
James Bond	29	202.8	354.1	406.7	576.7 (±175.5)	145.0%
Kangaroo	52	1622	8.8	3035	6740 (±2959)	224.2%
Krull	1598	3372	3341	2395	3805 (±1033)	277.0%
Kung-Fu Master	258.5	19544	29151	22736	23270 (±5955)	102.4%
Montezuma's Revenge	0	10.7	259	4367	0 (±0)	0.0%
Ms. Pacman	307.3	1692	1227	15693	2311 (±525)	13.0%
Name This Game	2292	2500	2247	4076	7257 (±547)	278.3%
Pong	-20.7	-19	-17.4	9.3	18.9 (±1.3)	132.0%
Private Eye	24.9	684.3	86	69571	1788 (±5473)	2.5%
Q*Bert	163.9	613.5	960.3	13455	10596 (±3294)	78.5%
River Raid	1339	1904	2650	13513	8316 (±1049)	57.3%
Road Runner	11.5	67.7	89.1	7845	18257 (±4268)	232.9%
Robotank	2.2	28.7	12.4	11.9	51.6 (±4.7)	509.0%
Seaquest	68.4	664.8	675.5	20182	5286 (±1310)	25.9%
Space Invaders	148	250.1	267.9	1652	1976 (±893)	121.5%
Star Gunner	664	1070	9.4	10250	57997 (±3152)	598.1%
Tennis	-23.8	-0.1	0	-8.9	-2.5 (±1.9)	143.2%
Time Pilot	3568	3741	24.9	5925	5947 (±1600)	100.9%
Tutankham	11.4	114.3	98.2	167.6	186.7 (±41.9)	112.2%
Up and Down	533.4	3533	2449	9082	8456 (±3162)	92.7%
Venture	0	66	0.6	1188	380 (±238.6)	32.0%
Video Pinball	16257	16871	19761	17298	42684 (±16287)	2539.4%
Wizard of Wor	563.5	1981	36.9	4757	3393 (±2019)	67.5%
Zaxxon	32.5	3365	21.4	9173	4977 (±1235)	54.1%"""

nature_rows = mnih_extended_table_2.split("\n")[1:]
name_re = re.compile(r'[^0-9\t]+')
for row in nature_rows:
    match = name_re.match(row)
    game = game_metric_name(match.group(0))
    rest = name_re.sub("", row, 1)
    cols = rest.split()
    random, bll, sarsa, human, dqn, dqn_err, norm = cols
    dqn, sarsa, bll = float(dqn), float(sarsa), float(bll)
    dqn_err = float(re.search("[0-9]+", dqn_err).group(0))
    globals()[game].measure(date(2015, 2, 26), dqn, 'Nature DQN', 
        url='https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf', 
        papername="Human-level control through deep reinforcement learning", 
        uncertainty=dqn_err)
    globals()[game].performance_floor = float(random)
    # The Mnih et al. Nature paper attributes these SARSA results to this paper,
    # but the paper doesn't actually seem to include them?
    globals()[game].measure(date(2012, 7, 14), sarsa, 'SARSA', 
        url='https://www.aaai.org/ocs/index.php/AAAI/AAAI12/paper/view/5162',
        papername="Investigating Contingency Awareness Using Atari 2600 Games")

    globals()[game].measure(None, bll, 'Best linear', 
        url='https://arxiv.org/abs/1207.4708v1')
    if verb:
        print("{0}.measure(None, {1}, 'Nature DQN', papername='Human-level control through deep reinforcement learning' "
              "url='https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf'"
              ", uncertainty={2})".format(game, dqn, dqn_err))


a3c_table_s3 = """Game	DQN	Gorila	Double	Dueling	Prioritized	A3C FF, 1 day	A3C FF	A3C LSTM
Alien	570.2	813.5	1033.4	1486.5	900.5	182.1	518.4	945.3
Amidar	133.4	189.2	169.1	172.7	218.4	283.9	263.9	173.0
Assault	3332.3	1195.8	6060.8	3994.8	7748.5	3746.1	5474.9	14497.9
Asterix	124.5	3324.7	16837.0	15840.0	31907.5	6723.0	22140.5	17244.5
Asteroids	697.1	933.6	1193.2	2035.4	1654.0	3009.4	4474.5	5093.1
Atlantis	76108.0	629166.5	319688.0	445360.0	593642.0	772392.0	911091.0	875822.0
Bank Heist	176.3	399.4	886.0	1129.3	816.8	946.0	970.1	932.8
Battle Zone	17560.0	19938.0	24740.0	31320.0	29100.0	11340.0	12950.0	20760.0
Beam Rider	8672.4	3822.1	17417.2	14591.3	26172.7	13235.9	22707.9	24622.2
Berzerk			1011.1	910.6	1165.6	1433.4	817.9	862.2
Bowling	41.2	54.0	69.6	65.7	65.8	36.2	35.1	41.8
Boxing	25.8	74.2	73.5	77.3	68.6	33.7	59.8	37.3
Breakout	303.9	313.0	368.9	411.6	371.6	551.6	681.9	766.8
Centipede	3773.1	6296.9	3853.5	4881.0	3421.9	3306.5	3755.8	1997.0
Chopper Command	3046.0	3191.8	3495.0	3784.0	6604.0	4669.0	7021.0	10150.0
Crazy Climber	50992.0	65451.0	113782.0	124566.0	131086.0	101624.0	112646.0	138518.0
Defender			27510.0	33996.0	21093.5	36242.5	56533.0	233021.5
Demon Attack	12835.2	14880.1	69803.4	56322.8	73185.8	84997.5	113308.4	115201.9
Double Dunk	-21.6	-11.3	-0.3	-0.8	2.7	0.1	-0.1	0.1
Enduro	475.6	71.0	1216.6	2077.4	1884.4	-82.2	-82.5	-82.5
Fishing Derby	-2.3	4.6	3.2	-4.1	9.2	13.6	18.8	22.6
Freeway	25.8	10.2	28.8	0.2	27.9	0.1	0.1	0.1
Frostbite	157.4	426.6	1448.1	2332.4	2930.2	180.1	190.5	197.6
Gopher	2731.8	4373.0	15253.0	20051.4	57783.8	8442.8	10022.8	17106.8
Gravitar	216.5	538.4	200.5	297.0	218.0	269.5	303.5	320.0
H.E.R.O.	12952.5	8963.4	14892.5	15207.9	20506.4	28765.8	32464.1	28889.5
Ice Hockey	-3.8	-1.7	-2.5	-1.3	-1.0	-4.7	-2.8	-1.7
James Bond	348.5	444.0	573.0	835.5	3511.5	351.5	541.0	613.0
Kangaroo	2696.0	1431.0	11204.0	10334.0	10241.0	106.0	94.0	125.0
Krull	3864.0	6363.1	6796.1	8051.6	7406.5	8066.6	5560.0	5911.4
Kung-Fu Master	11875.0	20620.0	30207.0	24288.0	31244.0	3046.0	28819.0	40835.0
Montezuma’s Revenge	50.0	84.0	42.0	22.0	13.0	53.0	67.0	41.0
Ms. Pacman	763.5	1263.0	1241.3	2250.6	1824.6	594.4	653.7	850.7
Name This Game	5439.9	9238.5	8960.3	11185.1	11836.1	5614.0	10476.1	12093.7
Phoenix			12366.5	20410.5	27430.1	28181.8	52894.1	74786.7
Pit Fall			-186.7	-46.9	-14.8	-123.0	-78.5	-135.7
Pong	16.2	16.7	19.1	18.8	18.9	11.4	5.6	10.7
Private Eye	298.2	2598.6	-575.5	292.6	179.0	194.4	206.9	421.1
Q*Bert	4589.8	7089.8	11020.8	14175.8	11277.0	13752.3	15148.8	21307.5
River Raid	4065.3	5310.3	10838.4	16569.4	18184.4	10001.2	12201.8	6591.9
Road Runner	9264.0	43079.8	43156.0	58549.0	56990.0	31769.0	34216.0	73949.0
Robotank	58.5	61.8	59.1	62.0	55.4	2.3	32.8	2.6
Seaquest	2793.9	10145.9	14498.0	37361.6	39096.7	2300.2	2355.4	1326.1
Skiing			-11490.4	-11928.0	-10852.8	-13700.0	-10911.1	-14863.8
Solaris			810.0	1768.4	2238.2	1884.8	1956.0	1936.4
Space Invaders	1449.7	1183.3	2628.7	5993.1	9063.0	2214.7	15730.5	23846.0
Star Gunner	34081.0	14919.2	58365.0	90804.0	51959.0	64393.0	138218.0	164766.0
Surround			1.9	4.0	-0.9	-9.6	-9.7	-8.3
Tennis	-2.3	-0.7	-7.8	4.4	-2.0	-10.2	-6.3	-6.4
Time Pilot	5640.0	8267.8	6608.0	6601.0	7448.0	5825.0	12679.0	27202.0
Tutankham	32.4	118.5	92.2	48.0	33.6	26.1	156.3	144.2
Up and Down	3311.3	8747.7	19086.9	24759.2	29443.7	54525.4	74705.7	105728.7
Venture	54.0	523.4	21.0	200.0	244.0	19.0	23.0	25.0
Video Pinball	20228.1	112093.4	367823.7	110976.2	374886.9	185852.6	331628.1	470310.5
Wizard of Wor	246.0	10431.0	6201.0	7054.0	7451.0	5278.0	17244.0	18082.0
Yars Revenge			6270.6	25976.5	5965.1	7270.8	7157.5	5615.5
Zaxxon	831.0	6159.4	8593.0	10164.0	9501.0	2659.0	24622.0	23519.0"""

# Caption:
# Table S3. Raw scores for the human start condition (30 minutes emulator time). DQN scores taken from (Nair et al.,
# 2015). Double DQN scores taken from (Van Hasselt et al., 2015), Dueling scores from (Wang et al., 2015) and
# Prioritized scores taken from (Schaul et al., 2015)

a3c_rows = a3c_table_s3.split("\n")[1:]
for row in a3c_rows:
    cols = row.split("\t")
    game, dqn, gorila, ddqn, duel, prior, a3c_ff_1, a3c_ff, a3c_lstm = cols
    game1 = game_metric_name(game)
    metric = get_game_metric(game1, game, None, None)
    for alg, score in [("A3C FF (1 day) hs", a3c_ff_1), ("A3C FF hs", a3c_ff), ("A3C LSTM hs", a3c_lstm)]:
        score = float(score)
        metric.measure(None, score, alg, url="https://arxiv.org/abs/1602.01783")
        if verb: print('{0}.measure(None, {1}, "{2}", url="{3}")'.format(game1, score, alg, "https://arxiv.org/abs/1602.01783"))

    try:
        score = float(gorila)
        metric.measure(None, score, "Gorila", url="https://arxiv.org/abs/1507.04296")
        if verb: print('{0}.measure(None, {1}, "Gorila", url="{2}")'.format(game1, score, "https://arxiv.org/abs/1507.04296"))
    except ValueError:
        if verb: print("No Gorila score for", game)


def snarf_row_oriented_table(raw_table, algorithm_pairs, paper_url):
    """Ingest a table of row oriented results

    algorithm_pairs -- [(alg_name, col_index)]
    """
    rows = raw_table.split("\n")[1:]
    for row in rows:
        cols = row.split("\t")
        game = cols[0]
        game1 = game_metric_name(game)
        metric = get_game_metric(game1, game, None, None)
        for alg, idx in algorithm_pairs:
            score = float(cols[idx])
            metric.measure(None, score, alg, url=paper_url)
            if verb:
                print('{0}.measure(None, {1}, "{2}", url="{3}")'.format(game1, score, alg, paper_url))


cts_tabe_2 = """DQN	A3C-CTS	Prior Duel	DQN-CTS	DQN-PixelCNN
FREEWAY	30.8	30.48	33.0	31.7	31.7
GRAVITAR	473.0	238.68	238.0	498.3	859.1
MONTEZUMA’S REVENGE	0.0	273.70	0.0	3705.5	2514.3
PITFALL!	-286.1	-259.09	0.0	0.0	0.0
PRIVATE EYE	146.7	99.32	206.0	8358.7	15806.5
SOLARIS	3,482.8	2270.15	133.4	2863.6	5501.5
VENTURE	163.0	0.00	48.0	82.2	1356.25"""

snarf_row_oriented_table(cts_tabe_2, [("DQN-CTS", 3), ("DQN-PixelCNN", 4)], "https://arxiv.org/abs/1703.01310v1")
snarf_row_oriented_table(cts_tabe_2, [("A3C-CTS", 2)], "https://arxiv.org/abs/1606.01868")


# Schrittweiser 2020

ape_x_source = "https://arxiv.org/pdf/1803.00933.pdf"
ape_x_date = date(2018, 3, 2)
ape_x_papername = "DISTRIBUTED PRIORITIZED EXPERIENCE REPLAY"

r2d2_source = "https://openreview.net/pdf?id=r1lyTjAqYX"
r2d2_date = date(2018, 9, 27)
r2d2_papername = "Recurrent Experience Replay in Distributed Reinforcement Learning"

simple_source = "https://arxiv.org/pdf/1903.00374.pdf"
simple_date = date(2020, 2, 19)
simple_papername = "MODEL BASED REINFORCEMENT LEARNING FOR ATARI"

muzero_source = "https://arxiv.org/pdf/1911.08265v2.pdf"
muzero_date = date(2020, 2, 21)
muzero_papername = "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model"

# A few names were tweaked to match the metric names
schrittweiser2020_table_S2 = """Game	Random	Human	Ape-X [18]	MuZero	MuZero normalized
alien	128.30	6371.30	17732.00	713387.37	11424.9
amidar	11.79	1540.43	1047.00	26638.80	1741.9
assault	166.95	628.89	24405.00	143900.58	31115.2
asterix	164.50	7536.00	283180.00	985801.95	13370.9
asteroids	877.10	36517.30	117303.00	606971.12	1700.6
atlantis	13463.00	26575.00	918715.00	1653202.50	12505.6
bank heist	21.70	644.50	1201.00	962.11	151.0
battle zone	3560.00	33030.00	92275.00	791387.00	2673.3
beam rider	254.56	14961.02	72234.00	419460.76	2850.5
berzerk	196.10	2237.50	55599.00	87308.60	4267.3
bowling	35.16	146.46	30.00	194.03	142.7
boxing	-1.46	9.61	81.00	56.60	524.5
breakout	1.77	27.86	757.00	849.59	3249.6
centipede	1925.45	10321.89	5712.00	1138294.60	13533.9
chopper command	644.00	8930.00	576602.00	932370.10	11244.6
crazy climber	9337.00	32667.00	263954.00	412213.90	1726.9
defender	1965.50	14296.00	399865.00	823636.00	6663.7
demon attack	208.25	3442.85	133002.00	143858.05	4441.0
double dunk	-15.97	-14.37	22.00	23.12	2443.1
enduro	-81.84	740.17	2042.00	2264.20	285.4
fishing derby	-77.11	5.09	22.00	57.45	163.7
freeway	0.17	25.61	29.00	28.38	110.9
frostbite	90.80	4202.80	6512.00	613944.04	14928.3
gopher	250.00	2311.00	121168.00	129218.68	6257.6
gravitar	245.50	3116.00	662.00	3390.65	109.6
hero	1580.30	25839.40	26345.00	44129.55	175.4
ice hockey	-9.67	0.53	24.00	52.40	608.5
james bond	33.50	368.50	18992.00	39107.20	11663.8
kangaroo	100.00	2739.00	578.00	13210.50	496.8
krull	1151.90	2109.10	8592.00	257706.70	26802.6
kung-fu master	304.00	20786.80	72068.00	174623.60	851.1
montezuma's revenge	25.00	4182.00	1079.00	57.10	0.8
ms. pacman	197.80	15375.05	6135.00	230650.24	1518.4
name this game	1747.80	6796.00	23830.00	152723.62	2990.7
phoenix	1134.40	6686.20	188789.00	943255.07	16969.6
pitfall	-348.80	5998.91	-273.00	-801.10	-7.1
pong	-17.95	15.46	19.00	19.20	111.2
private eye	662.78	64169.07	865.00	5067.59	6.9
q*bert	159.38	12085.00	380152.00	39302.10	328.2
river raid	588.30	14382.20	49983.00	315353.33	2281.9
road runner	200.00	6878.00	127112.00	580445.00	8688.9
robotank	2.42	8.94	69.00	128.80	1938.3
seaquest	215.50	40425.80	377180.00	997601.01	2480.4
skiing	-15287.35	-3686.58	-11359.00	-29400.75	-121.7
solaris	2047.20	11032.60	3116.00	2108.08	0.7
space invaders	182.55	1464.90	50699.00	57450.41	4465.9
star gunner	697.00	9528.00	432958.00	539342.70	6099.5
surround	-9.72	5.37	6.00	8.46	120.5
tennis	-21.43	-6.69	23.00	-2.30	129.8
time pilot	3273.00	5650.00	71543.00	405829.30	16935.5
tutankham	12.74	138.30	128.00	351.76	270.0
up and down	707.20	9896.10	347912.00	607807.85	6606.9
venture	18.00	1039.00	936.00	21.10	0.3
video pinball	0.00	15641.09	873989.00	970881.10	6207.2
wizard of wor	804.00	4556.00	46897.00	196279.20	5209.9
yars revenge	1476.88	47135.17	131701.00	888633.84	1943.0
zaxxon	475.00	8443.00	37672.00	592238.70	7426.8"""

# Game	Random	Human	SimPLe [20]	Ape-X [18]	R2D2 [21]	MuZero	MuZero normalized
schrittweiser2020_table_S1 = """alien	227.75	7127.80	616.90	40805.00	229496.90	741812.63	10747.5
amidar	5.77	1719.53	74.30	8659.00	29321.40	28634.39	1670.5
assault	222.39	742.00	527.20	24559.00	108197.00	143972.03	27664.9
asterix	210.00	8503.33	1128.30	313305.00	999153.30	998425.00	12036.4
asteroids	719.10	47388.67	793.60	155495.00	357867.70	678558.64	1452.4
atlantis	12850.00	29028.13	20992.50	944498.00	1620764.00	1674767.20	10272.6
bank heist	14.20	753.13	34.20	1716.00	24235.90	1278.98	171.2
battle zone	2360.00	37187.50	4031.20	98895.00	751880.00	848623.00	2429.9
beam rider	363.88	16926.53	621.60	63305.00	188257.40	454993.53	2744.9
berzerk	123.65	2630.42	-	57197.00	53318.70	85932.60	3423.1
bowling	23.11	160.73	30.00	18.00	219.50	260.13	172.2
boxing	0.05	12.06	7.80	100.00	98.50	100.00	832.2
breakout	1.72	30.47	16.40	801.00	837.70	864.00	2999.2
centipede	2090.87	12017.04	-	12974.00	599140.30	1159049.27	11655.6
chopper command	811.00	7387.80	979.40	721851.00	986652.00	991039.70	15056.4
crazy climber	10780.50	35829.41	62583.60	320426.00	366690.70	458315.40	1786.6
defender	2874.50	18688.89	-	411944.00	665792.00	839642.95	5291.2
demon attack	152.07	1971.00	208.10	133086.00	140002.30	143964.26	7906.4
double dunk	-18.55	-16.40	-	24.00	23.70	23.94	1976.3
enduro	0.00	860.53	-	2177.00	2372.70	2382.44	276.9
fishing derby	-91.71	-38.80	-90.70	44.00	85.80	91.16	345.6
freeway	0.01	29.60	16.70	34.00	32.50	33.03	111.6
frostbite	65.20	4334.67	236.90	9329.00	315456.40	631378.53	14786.7
gopher	257.60	2412.50	596.80	120501.00	124776.30	130345.58	6036.8
gravitar	173.00	3351.43	173.40	1599.00	15680.70	6682.70	204.8
hero	1026.97	30826.38	2656.60	31656.00	39537.10	49244.11	161.8
ice hockey	-11.15	0.88	-11.60	33.00	79.30	67.04	650.0
jamesbond	29.00	302.80	100.50	21323.00	25354.00	41063.25	14986.9
kangaroo	52.00	3035.00	51.20	1416.00	14130.70	16763.60	560.2
krull	1598.05	2665.53	2204.80	11741.00	218448.10	269358.27	25083.4
kung fu master	258.50	22736.25	14862.50	97830.00	233413.30	204824.00	910.1
montezuma revenge	0.00	4753.33	-	2500.00	2061.30	0.00	0.0
ms pacman	307.30	6951.60	1480.00	11255.00	42281.70	243401.10	3658.7
name this game	2292.35	8049.00	2420.70	25783.00	58182.70	157177.85	2690.5
phoenix	761.40	7242.60	-	224491.00	864020.00	955137.84	14725.3
pitfall	-229.44	6463.69	-	-1.00	0.00	0.00	3.4
pong	-20.71	14.59	12.80	21.00	21.00	21.00	118.2
private eye	24.94	69571.27	35.00	50.00	5322.70	15299.98	22.0
qbert	163.88	13455.00	1288.80	302391.00	408850.00	72276.00	542.6
riverraid	1338.50	17118.00	1957.80	63864.00	45632.10	323417.18	2041.1
road runner	11.50	7845.00	5640.60	222235.00	599246.70	613411.80	7830.5
robotank	2.16	11.94	-	74.00	100.40	131.13	1318.7
seaquest	68.40	42054.71	683.30	392952.00	999996.70	999976.52	2381.5
skiing	-17098.09	-4336.93	-	-10790.00	-30021.70	-29968.36	-100.9
solaris	1236.30	12326.67	-	2893.00	3787.20	56.62	-10.6
space invaders	148.03	1668.67	-	54681.00	43223.40	74335.30	4878.7
star gunner	664.00	10250.00	-	434343.00	717344.00	549271.70	5723.0
surround	-9.99	6.53	-	7.00	9.90	9.99	120.9
tennis	-23.84	-8.27	-	24.00	-0.10	0.00	153.1
time pilot	3568.00	5229.10	-	87085.00	445377.30	476763.90	28486.9
tutankham	11.43	167.59	-	273.00	395.30	491.48	307.4
up n down	533.40	11693.23	3350.30	401884.00	589226.90	715545.61	6407.0
venture	0.00	1187.50	-	1813.00	1970.70	0.40	0.0
video pinball	0.00	17667.90	-	565163.00	999383.20	981791.88	5556.9
wizard of wor	563.50	4756.52	-	46204.00	144362.70	197126.00	4687.9
yars revenge	3092.91	54576.93	5664.30	148595.00	995048.40	553311.46	1068.7
zaxxon	32.50	9173.30	-	42286.00	224910.70	725853.90	7940.5"""

mu_zero_rows = schrittweiser2020_table_S1.split("\n")

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

for row in mu_zero_rows[1:]:
    cols = row.split("\t")
    game, random, human, simple, ape_x, r2d2, muzero, muzero_norm = cols
    # matching_metrics = [x for x in globals().get("problems")["Simple video games"].metrics if game.lower() in x.name.lower()]
    game_name = game_metric_name(game)
    matching_metric_keys = [x for x in globals() if "_metric" in x and game_name in x.lower()]
    if len(matching_metric_keys) == 1:
        if is_float(simple.strip()):
            globals()[matching_metric_keys[0]].measure(simple_date, float(simple), "SimPLe " + game,
                                        url=simple_source,
                                        papername=simple_papername)
        if is_float(ape_x.strip()):
            globals()[matching_metric_keys[0]].measure(ape_x_date, float(ape_x), "Ape-X " + game,
                                        url=ape_x_source,
                                        papername=ape_x_papername)
        if is_float(ape_x.strip()):
            globals()[matching_metric_keys[0]].measure(r2d2_date, float(r2d2), "R2D2 " + game,
                                        url=r2d2_source,
                                        papername=r2d2_papername)
        if is_float(r2d2.strip()):
            globals()[matching_metric_keys[0]].measure(muzero_date, float(muzero), "MuZero " + game,
                                        url=muzero_source,
                                        papername=muzero_papername)
    else:
        print(f"{game} had {len(matching_metric_keys)} matches")

# vim: set list:listchars=tab:!·,trail:·

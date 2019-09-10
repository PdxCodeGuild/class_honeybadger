


import re




text = '''
Chapter I
                                Boyhood


The contemplation of the wonders of the universe is always inspiring and
upliftingâ€”the crystalline purity of the sky, the splendor of the sunrise
and sunset, the grandeur of the starry night, the fragrant forest, the
smiling landscape, the tree, the flower, the boundless ocean, and all
the countless manifestations of nature. But how much greater our
admiration and inspiration when we reverently contemplate the progress
of a noble human soul toward ever higher and higher planes of
perfection! Some of the good seed which it scatters may take root in our
minds to strengthen and develop the best that is in us. We perceive the
possibilities of the race and what we may ourselves become if the will
to strive keeps pace with a love for what is good.

In ancient times thoughtful people compared great and good souls to the
stars. They rise in the spiritual firmament with a pure radiance and,
ever anew breaking through the mists and clouds which obscure them,
remain visible to later generations. Thus they become guiding stars for
struggling human beings here below. The particular star which the reader
who has the wisdom and the inclination to perfect himself is invited to
study in these pages arose in the forests of Virginia on the
twenty-second of February, 1732. It was there that little George first
opened his eyes and looked out upon a world in which he was to play so
great a part. There his negro mammy sat with him on the bench before the
door, throwing crumbs to the turkeys and pigeons to amuse him, and
there, under the rustling trees, he whittled his first horse out of
hazelwood.

Georgeâ€™s father, Augustine Washington, was a planter of English
extraction. His first ancestor had emigrated from England when North
America was still the undisputed property of the Indians. The territory
which later became the United States is almost as large as the continent
of Europe. Two hundred years ago the whole country was a trackless
forest, broken only by enormous morasses, cane-brakes, and savannas or
grassy prairies. In the prosperous plantation house on the east bank of
the Rappahannock in which George was born, piety, industry, and probity
had made their habitation. That was the first blessing with which heaven
dowered the boy. Of course, living in a pure and healthy moral
atmosphere is not in itself all that is required to guide a youth into
paths of rectitude; the will to do the right and the continual struggle
to attain it can alone accomplish the greater part. Reprobates have
sometimes come out of the best environments. The voice of conscience is
awakened very early in the human breast and we soon know right from
wrong. However, it is a great boon and a wonderful help to be surrounded
by people who are examples of virtue in word and deed, and he who strays
into the paths of sin in spite of such surroundings is doubly to be
censured.

At that time the English immigrants lived scattered in the forest, but
neighbors had already formed themselves into parishes and founded
schools and churches. The schools were of course of a very simple type,
nothing but reading, writing, and arithmetic being taught. Most of the
settlers found this quite sufficient for their children and rich
planters sent their sons to England to be educated. Lawrence Washington,
Georgeâ€™s eldest step-brother, enjoyed these advantages. He was fourteen
years older than George, who was a babe in arms when Lawrence set out on
his first voyage to England, so that he could not remember his
step-brother. When George was eight years old, Lawrence, now in his
twenty-second year, returned. The arrival of the well-educated and
well-bred young gentleman was a welcome event in the family circle, and
George loved him from the first moment. Their affection was mutual, and
indeed Lawrence showed a truly paternal interest in the bright, alert
boy.

Their father had no intention of sending another son abroad. He looked
upon Lawrence as the natural head of the family after his death and was
satisfied that his probable successor had received a liberal education.
Accordingly George was sent to the parish school. He applied himself
eagerly to his tasks and thus laid a firm foundation, at least, for the
studies which he afterward prosecuted by himself. One trait of his
character showed itself very earlyâ€”he did all his work with the greatest
conscientiousness and neatness. Not a stroke of his pen betrayed
carelessness. Some of his school books, which have been preserved, bear
witness to this. He showed the same care when any work about the house
was required of him. He endeavored to do whatever he had to do, however
insignificant it was or might seem to be, as perfectly as possible. Of
course he was not capable of appreciating at that time how important
this was in the development of his character. It was simply his early
awakened sense of duty, reinforced by his earnest efforts to practise
what he knew to be right. It was not until later that he realized the
deeper significance of work as a means of strengthening the powers of
the soul. There is no kind of work which may not be either well or ill
done. If you put all your capabilities into it, and the result is more
or less satisfactory, you have accomplished even more than the success
of the moment; you have been working for the growth of your inner self.
For one who realizes this, the greatest drudgery has lost its sting.
George was just as conscientious in everything which pertained to
morals. He had a passionate disposition, but we learn that early in life
he strove to curb his hasty temper by exercising deliberation and will
power. It was therefore customary, among his school-fellows, when
disagreements arose, to take them to him, and his verdict was generally
accepted, for they knew that he was willing to acknowledge himself in
the wrong when his fiery temper had carried him away. It was justice and
not the person that had weight with him.

Another of his qualities, military talent, was early recognizable. It
was an inheritance. There had been warriors among his ancestors, men of
note, of whom English chronicles tell us. Several of these had so
distinguished themselves as to have been knighted. Georgeâ€™s brother
Lawrence was of a like temper, and it now happened that he had an
opportunity of becoming a soldier. British commerce in the West Indies
had suffered heavy losses through piratical attacks by Spain and the
English government determined to avenge itself. A fleet was fitted out,
and as England was the mother country of the Virginians, the recruiting
drum was heard in the colony also. Lawrence volunteered and was given a
captainâ€™s commission. It was no wonder that there was considerable
excitement over all this in the home of the Washingtons. George took the
liveliest interest in his brotherâ€™s equipment. He thought it very proper
that the robbers, of whom he had heard many dreadful stories, should be
punished, and gazed at his brotherâ€™s bright sword with delight and
respect. He vowed that he too would sometime help to right the wrongs of
his injured countrymen in time of need. He was told many tales of his
valiant ancestors. It is no wonder then that the picture of his brother
as he had left home, in his war trappings, was constantly in his mind;
nor that he begged for his letters, after his father had read them to
the assembled family, to pore over them, especially when they had
something to tell of the soldierâ€™s adventures.
'''

pattern = '[a-zA-Z-â€™]+'


print(re.findall(pattern, text))

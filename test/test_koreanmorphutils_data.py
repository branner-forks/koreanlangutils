# -*- coding: utf-8 -*-

# This is an automatically generated file that uses cvurrent code to make expected results.
# You can edit the file (especially to change incorrect to correct expected results)
# but if you do the edits will be lost when you regenerate the file and will
# have to be reapplied.  For this reason It is recommended that you regenerate the file only
# when you believe that all the results will be correct.  


    
test_getEndingAdderForStem_data = [
    #(stem,irr,expectedEndingAdderName)
    (u'가',None,'RegVEndingAdder'),
    (u'하',None,'RegVEndingAdder'),
    (u'말하',None,'RegVEndingAdder'),
    (u'내',None,'RegVEndingAdder'),
    (u'건네',None,'RegVEndingAdder'),
    (u'서',None,'RegVEndingAdder'),
    (u'그러',None,'RegVEndingAdder'),
    (u'켜',None,'RegVEndingAdder'),
    (u'크',None,'RegVEndingAdder'),
    (u'바쁘',None,'RegVEndingAdder'),
    (u'모으',None,'RegVEndingAdder'),
    (u'보',None,'RegVEndingAdder'),
    (u'주',None,'RegVEndingAdder'),
    (u'푸',None,'RegVEndingAdder'),
    (u'비',None,'RegVEndingAdder'),
    (u'치',None,'RegVEndingAdder'),
    (u'벌이',None,'RegVEndingAdder'),
    (u'보이',None,'RegVEndingAdder'),
    (u'쉬',None,'RegVEndingAdder'),
    (u'희',None,'RegVEndingAdder'),
    (u'되',None,'RegVEndingAdder'),
    (u'받',None,'RegCEndingAdder'),
    (u'먹',None,'RegCEndingAdder'),
    (u'살',None,'RegLEndingAdder'),
    (u'걸',None,'RegLEndingAdder'),
    (u'돕','irrb','IrrBEndingAdder'),
    (u'고맙','irrb','IrrBEndingAdder'),
    (u'눕','irrb','IrrBEndingAdder'),
    (u'뵙','irrb2','IrrB2EndingAdder'),
    (u'뵙',None,'IrrB2EndingAdder'),
    (u'낫','irrs','IrrSEndingAdder'),
    (u'깃','irrs','IrrSEndingAdder'),
    (u'캐닫','irrd','IrrDEndingAdder'),
    (u'걷','irrd','IrrDEndingAdder'),
    (u'노랗','irrh','IrrHEndingAdder'),
    (u'그렇','irrh','IrrHEndingAdder'),
    (u'오르','irrlu','IrrLUEndingAdder'),
    (u'부르','irrlu','IrrLUEndingAdder'),
    (u'이르','irrle','IrrLEEndingAdder'),
    (u'사람','cop','CopulaEndingAdder'),
    (u'의사','cop','CopulaEndingAdder'),
    (u'것','cop','CopulaEndingAdder'),
    (u'거','cop','CopulaEndingAdder'),
    (u'아니','cop','CopulaEndingAdder'),
    ]


    
test_determineEndingType_data = [
    #(postC,postV,expectedEndingType,expectedPostV)
    (u'다',None,'ONE_SHAPE',u'다'),
    (u'니',None,'ONE_SHAPE_DROP_L',u'니'),
    (u'으니',None,'TWO_SHAPE_REG',u'니'),
    (u'세',None,'ONE_SHAPE_DROP_L',u'세'),
    (u'으면',None,'TWO_SHAPE_REG',u'면'),
    (u'음',None,'TWO_SHAPE_REG',u'ㅁ'),
    (u'으러',None,'TWO_SHAPE_REG',u'러'),
    (u'을지',None,'TWO_SHAPE_REG',u'ㄹ지'),
    (u'을',None,'TWO_SHAPE_REG',u'ㄹ'),
    (u'습니다',u'ㅂ니다','TWO_SHAPE_IRR',u'ㅂ니다'),
    (u'소',u'오','TWO_SHAPE_IRR',u'오'),
    (u'아~어/E-conjunctive',None,'INF_BASED',u'아~어/E-conjunctive'),
    (u'아서~어서/E-conjunctive',None,'INF_BASED',u'아서~어서/E-conjunctive'),
    (u'아~어/E-s-ender',None,'INF_BASED',u'아~어/E-s-ender'),
    (u'아요~어요/E-s-ender',None,'INF_BASED',u'아요~어요/E-s-ender'),
    (u'았어요~었어요',None,'INF_BASED',u'았어요~었어요'),
    (u'다/E-quote',None,'ONE_SHAPE',u'다/E-quote'),
    (u'대/E-quote',None,'ONE_SHAPE',u'대/E-quote'),
    (u'으냐고/E-quote',None,'TWO_SHAPE_REG',u'냐고/E-quote'),
    ]

test_addParticle_data = [
    #(word,postC,postV,expectedWordPlusParticle)
    (u'말',u'으로',None,u'말로'),
    (u'말',u'이랑',None,u'말이랑'),
    (u'말',u'도',None,u'말도'),
    (u'말',u'에게',None,u'말에게'),
    (u'말',u'이',u'가',u'말이'),
    (u'말',u'과',u'와',u'말과'),
    (u'말',u'을',u'를',u'말을'),
    (u'닭',u'으로',None,u'닭으로'),
    (u'닭',u'이랑',None,u'닭이랑'),
    (u'닭',u'도',None,u'닭도'),
    (u'닭',u'에게',None,u'닭에게'),
    (u'닭',u'이',u'가',u'닭이'),
    (u'닭',u'과',u'와',u'닭과'),
    (u'닭',u'을',u'를',u'닭을'),
    (u'개',u'으로',None,u'개로'),
    (u'개',u'이랑',None,u'개랑'),
    (u'개',u'도',None,u'개도'),
    (u'개',u'에게',None,u'개에게'),
    (u'개',u'이',u'가',u'개가'),
    (u'개',u'과',u'와',u'개와'),
    (u'개',u'을',u'를',u'개를'),
    ]

test_makeInfinitive_data = [
    #(stem,irr,inf,infMaxVariants)
    (u'가',None,u'가',u'가'),
    (u'하',None,u'해,하여',u'해,하여'),
    (u'말하',None,u'말해,말하여',u'말해,말하여'),
    (u'내',None,u'내,내어',u'내,내어'),
    (u'건네',None,u'건네',u'건네'),
    (u'서',None,u'서',u'서'),
    (u'그러',None,u'그래',u'그래'),
    (u'켜',None,u'켜',u'켜'),
    (u'크',None,u'커',u'커'),
    (u'바쁘',None,u'바빠',u'바빠,바뻐'),
    (u'모으',None,u'모아',u'모아'),
    (u'보',None,u'봐,보아',u'봐,보아'),
    (u'주',None,u'줘,주어',u'줘,주어'),
    (u'푸',None,u'퍼',u'퍼'),
    (u'비',None,u'비어',u'비어'),
    (u'치',None,u'쳐,치어',u'쳐,치어'),
    (u'벌이',None,u'벌여',u'벌여,벌이어'),
    (u'보이',None,u'보여',u'보여,보이어'),
    (u'쉬',None,u'쉬어',u'쉬어'),
    (u'희',None,u'희어',u'희어'),
    (u'되',None,u'돼,되어',u'돼,되어'),
    (u'받',None,u'받아',u'받아,받어'),
    (u'먹',None,u'먹어',u'먹어'),
    (u'살',None,u'살아',u'살아,살어'),
    (u'걸',None,u'걸어',u'걸어'),
    (u'돕','irrb',u'도와',u'도와'),
    (u'고맙','irrb',u'고마워',u'고마와,고마워'),
    (u'눕','irrb',u'누워',u'누워'),
    (u'뵙','irrb2',u'봬,뵈어',u'봬,뵈어'),
    (u'뵙',None,u'봬,뵈어',u'봬,뵈어'),
    (u'낫','irrs',u'나아',u'나아,나어'),
    (u'깃','irrs',u'기어',u'기어'),
    (u'캐닫','irrd',u'캐달아',u'캐달아,캐달어'),
    (u'걷','irrd',u'걸어',u'걸어'),
    (u'노랗','irrh',u'노래',u'노래'),
    (u'그렇','irrh',u'그래',u'그래'),
    (u'오르','irrlu',u'올라',u'올라'),
    (u'부르','irrlu',u'불러',u'불러'),
    (u'이르','irrle',u'이르러',u'이르러'),
    (u'사람','cop',u'사람이어',u'사람이어'),
    (u'의사','cop',u'의사여',u'의사여'),
    (u'것','cop',u'것이어',u'것이어'),
    (u'거','cop',u'거여',u'거여'),
    (u'아니','cop',u'아니여',u'아니여'),
    ]

test_addEnding_data = [
    #(stem,irr,postC,postV,expectedStemPlusEnding)

    (u'가',None,u'다',None,u'가다'),
    (u'가',None,u'니',None,u'가니'),
    (u'가',None,u'으니',None,u'가니'),
    (u'가',None,u'세',None,u'가세'),
    (u'가',None,u'으면',None,u'가면'),
    (u'가',None,u'음',None,u'감'),
    (u'가',None,u'으러',None,u'가러'),
    (u'가',None,u'을지',None,u'갈지'),
    (u'가',None,u'을',None,u'갈'),
    (u'가',None,u'습니다',u'ㅂ니다',u'갑니다'),
    (u'가',None,u'소',u'오',u'가오'),
    (u'가',None,u'아~어/E-conjunctive',None,u'가'),
    (u'가',None,u'아서~어서/E-conjunctive',None,u'가서'),
    (u'가',None,u'아~어/E-s-ender',None,u'가'),
    (u'가',None,u'아요~어요/E-s-ender',None,u'가요'),
    (u'가',None,u'았어요~었어요',None,u'갔어요'),
    (u'가',None,u'다/E-quote',None,u'가다'),
    (u'가',None,u'대/E-quote',None,u'가대'),
    (u'가',None,u'으냐고/E-quote',None,u'가냐고'),

    (u'하',None,u'다',None,u'하다'),
    (u'하',None,u'니',None,u'하니'),
    (u'하',None,u'으니',None,u'하니'),
    (u'하',None,u'세',None,u'하세'),
    (u'하',None,u'으면',None,u'하면'),
    (u'하',None,u'음',None,u'함'),
    (u'하',None,u'으러',None,u'하러'),
    (u'하',None,u'을지',None,u'할지'),
    (u'하',None,u'을',None,u'할'),
    (u'하',None,u'습니다',u'ㅂ니다',u'합니다'),
    (u'하',None,u'소',u'오',u'하오'),
    (u'하',None,u'아~어/E-conjunctive',None,u'해,하여'),
    (u'하',None,u'아서~어서/E-conjunctive',None,u'해서,하여서'),
    (u'하',None,u'아~어/E-s-ender',None,u'해'),
    (u'하',None,u'아요~어요/E-s-ender',None,u'해요'),
    (u'하',None,u'았어요~었어요',None,u'했어요,하였어요'),
    (u'하',None,u'다/E-quote',None,u'하다'),
    (u'하',None,u'대/E-quote',None,u'하대'),
    (u'하',None,u'으냐고/E-quote',None,u'하냐고'),

    (u'말하',None,u'다',None,u'말하다'),
    (u'말하',None,u'니',None,u'말하니'),
    (u'말하',None,u'으니',None,u'말하니'),
    (u'말하',None,u'세',None,u'말하세'),
    (u'말하',None,u'으면',None,u'말하면'),
    (u'말하',None,u'음',None,u'말함'),
    (u'말하',None,u'으러',None,u'말하러'),
    (u'말하',None,u'을지',None,u'말할지'),
    (u'말하',None,u'을',None,u'말할'),
    (u'말하',None,u'습니다',u'ㅂ니다',u'말합니다'),
    (u'말하',None,u'소',u'오',u'말하오'),
    (u'말하',None,u'아~어/E-conjunctive',None,u'말해,말하여'),
    (u'말하',None,u'아서~어서/E-conjunctive',None,u'말해서,말하여서'),
    (u'말하',None,u'아~어/E-s-ender',None,u'말해'),
    (u'말하',None,u'아요~어요/E-s-ender',None,u'말해요'),
    (u'말하',None,u'았어요~었어요',None,u'말했어요,말하였어요'),
    (u'말하',None,u'다/E-quote',None,u'말하다'),
    (u'말하',None,u'대/E-quote',None,u'말하대'),
    (u'말하',None,u'으냐고/E-quote',None,u'말하냐고'),

    (u'내',None,u'다',None,u'내다'),
    (u'내',None,u'니',None,u'내니'),
    (u'내',None,u'으니',None,u'내니'),
    (u'내',None,u'세',None,u'내세'),
    (u'내',None,u'으면',None,u'내면'),
    (u'내',None,u'음',None,u'냄'),
    (u'내',None,u'으러',None,u'내러'),
    (u'내',None,u'을지',None,u'낼지'),
    (u'내',None,u'을',None,u'낼'),
    (u'내',None,u'습니다',u'ㅂ니다',u'냅니다'),
    (u'내',None,u'소',u'오',u'내오'),
    (u'내',None,u'아~어/E-conjunctive',None,u'내,내어'),
    (u'내',None,u'아서~어서/E-conjunctive',None,u'내서,내어서'),
    (u'내',None,u'아~어/E-s-ender',None,u'내'),
    (u'내',None,u'아요~어요/E-s-ender',None,u'내요'),
    (u'내',None,u'았어요~었어요',None,u'냈어요,내었어요'),
    (u'내',None,u'다/E-quote',None,u'내다'),
    (u'내',None,u'대/E-quote',None,u'내대'),
    (u'내',None,u'으냐고/E-quote',None,u'내냐고'),

    (u'건네',None,u'다',None,u'건네다'),
    (u'건네',None,u'니',None,u'건네니'),
    (u'건네',None,u'으니',None,u'건네니'),
    (u'건네',None,u'세',None,u'건네세'),
    (u'건네',None,u'으면',None,u'건네면'),
    (u'건네',None,u'음',None,u'건넴'),
    (u'건네',None,u'으러',None,u'건네러'),
    (u'건네',None,u'을지',None,u'건넬지'),
    (u'건네',None,u'을',None,u'건넬'),
    (u'건네',None,u'습니다',u'ㅂ니다',u'건넵니다'),
    (u'건네',None,u'소',u'오',u'건네오'),
    (u'건네',None,u'아~어/E-conjunctive',None,u'건네'),
    (u'건네',None,u'아서~어서/E-conjunctive',None,u'건네서'),
    (u'건네',None,u'아~어/E-s-ender',None,u'건네'),
    (u'건네',None,u'아요~어요/E-s-ender',None,u'건네요'),
    (u'건네',None,u'았어요~었어요',None,u'건넸어요'),
    (u'건네',None,u'다/E-quote',None,u'건네다'),
    (u'건네',None,u'대/E-quote',None,u'건네대'),
    (u'건네',None,u'으냐고/E-quote',None,u'건네냐고'),

    (u'서',None,u'다',None,u'서다'),
    (u'서',None,u'니',None,u'서니'),
    (u'서',None,u'으니',None,u'서니'),
    (u'서',None,u'세',None,u'서세'),
    (u'서',None,u'으면',None,u'서면'),
    (u'서',None,u'음',None,u'섬'),
    (u'서',None,u'으러',None,u'서러'),
    (u'서',None,u'을지',None,u'설지'),
    (u'서',None,u'을',None,u'설'),
    (u'서',None,u'습니다',u'ㅂ니다',u'섭니다'),
    (u'서',None,u'소',u'오',u'서오'),
    (u'서',None,u'아~어/E-conjunctive',None,u'서'),
    (u'서',None,u'아서~어서/E-conjunctive',None,u'서서'),
    (u'서',None,u'아~어/E-s-ender',None,u'서'),
    (u'서',None,u'아요~어요/E-s-ender',None,u'서요'),
    (u'서',None,u'았어요~었어요',None,u'섰어요'),
    (u'서',None,u'다/E-quote',None,u'서다'),
    (u'서',None,u'대/E-quote',None,u'서대'),
    (u'서',None,u'으냐고/E-quote',None,u'서냐고'),

    (u'그러',None,u'다',None,u'그러다'),
    (u'그러',None,u'니',None,u'그러니'),
    (u'그러',None,u'으니',None,u'그러니'),
    (u'그러',None,u'세',None,u'그러세'),
    (u'그러',None,u'으면',None,u'그러면'),
    (u'그러',None,u'음',None,u'그럼'),
    (u'그러',None,u'으러',None,u'그러러'),
    (u'그러',None,u'을지',None,u'그럴지'),
    (u'그러',None,u'을',None,u'그럴'),
    (u'그러',None,u'습니다',u'ㅂ니다',u'그럽니다'),
    (u'그러',None,u'소',u'오',u'그러오'),
    (u'그러',None,u'아~어/E-conjunctive',None,u'그래'),
    (u'그러',None,u'아서~어서/E-conjunctive',None,u'그래서'),
    (u'그러',None,u'아~어/E-s-ender',None,u'그래'),
    (u'그러',None,u'아요~어요/E-s-ender',None,u'그래요'),
    (u'그러',None,u'았어요~었어요',None,u'그랬어요'),
    (u'그러',None,u'다/E-quote',None,u'그러다'),
    (u'그러',None,u'대/E-quote',None,u'그러대'),
    (u'그러',None,u'으냐고/E-quote',None,u'그러냐고'),

    (u'켜',None,u'다',None,u'켜다'),
    (u'켜',None,u'니',None,u'켜니'),
    (u'켜',None,u'으니',None,u'켜니'),
    (u'켜',None,u'세',None,u'켜세'),
    (u'켜',None,u'으면',None,u'켜면'),
    (u'켜',None,u'음',None,u'켬'),
    (u'켜',None,u'으러',None,u'켜러'),
    (u'켜',None,u'을지',None,u'켤지'),
    (u'켜',None,u'을',None,u'켤'),
    (u'켜',None,u'습니다',u'ㅂ니다',u'켭니다'),
    (u'켜',None,u'소',u'오',u'켜오'),
    (u'켜',None,u'아~어/E-conjunctive',None,u'켜'),
    (u'켜',None,u'아서~어서/E-conjunctive',None,u'켜서'),
    (u'켜',None,u'아~어/E-s-ender',None,u'켜'),
    (u'켜',None,u'아요~어요/E-s-ender',None,u'켜요'),
    (u'켜',None,u'았어요~었어요',None,u'켰어요'),
    (u'켜',None,u'다/E-quote',None,u'켜다'),
    (u'켜',None,u'대/E-quote',None,u'켜대'),
    (u'켜',None,u'으냐고/E-quote',None,u'켜냐고'),

    (u'크',None,u'다',None,u'크다'),
    (u'크',None,u'니',None,u'크니'),
    (u'크',None,u'으니',None,u'크니'),
    (u'크',None,u'세',None,u'크세'),
    (u'크',None,u'으면',None,u'크면'),
    (u'크',None,u'음',None,u'큼'),
    (u'크',None,u'으러',None,u'크러'),
    (u'크',None,u'을지',None,u'클지'),
    (u'크',None,u'을',None,u'클'),
    (u'크',None,u'습니다',u'ㅂ니다',u'큽니다'),
    (u'크',None,u'소',u'오',u'크오'),
    (u'크',None,u'아~어/E-conjunctive',None,u'커'),
    (u'크',None,u'아서~어서/E-conjunctive',None,u'커서'),
    (u'크',None,u'아~어/E-s-ender',None,u'커'),
    (u'크',None,u'아요~어요/E-s-ender',None,u'커요'),
    (u'크',None,u'았어요~었어요',None,u'컸어요'),
    (u'크',None,u'다/E-quote',None,u'크다'),
    (u'크',None,u'대/E-quote',None,u'크대'),
    (u'크',None,u'으냐고/E-quote',None,u'크냐고'),

    (u'바쁘',None,u'다',None,u'바쁘다'),
    (u'바쁘',None,u'니',None,u'바쁘니'),
    (u'바쁘',None,u'으니',None,u'바쁘니'),
    (u'바쁘',None,u'세',None,u'바쁘세'),
    (u'바쁘',None,u'으면',None,u'바쁘면'),
    (u'바쁘',None,u'음',None,u'바쁨'),
    (u'바쁘',None,u'으러',None,u'바쁘러'),
    (u'바쁘',None,u'을지',None,u'바쁠지'),
    (u'바쁘',None,u'을',None,u'바쁠'),
    (u'바쁘',None,u'습니다',u'ㅂ니다',u'바쁩니다'),
    (u'바쁘',None,u'소',u'오',u'바쁘오'),
    (u'바쁘',None,u'아~어/E-conjunctive',None,u'바빠'),
    (u'바쁘',None,u'아서~어서/E-conjunctive',None,u'바빠서'),
    (u'바쁘',None,u'아~어/E-s-ender',None,u'바빠'),
    (u'바쁘',None,u'아요~어요/E-s-ender',None,u'바빠요'),
    (u'바쁘',None,u'았어요~었어요',None,u'바빴어요'),
    (u'바쁘',None,u'다/E-quote',None,u'바쁘다'),
    (u'바쁘',None,u'대/E-quote',None,u'바쁘대'),
    (u'바쁘',None,u'으냐고/E-quote',None,u'바쁘냐고'),

    (u'모으',None,u'다',None,u'모으다'),
    (u'모으',None,u'니',None,u'모으니'),
    (u'모으',None,u'으니',None,u'모으니'),
    (u'모으',None,u'세',None,u'모으세'),
    (u'모으',None,u'으면',None,u'모으면'),
    (u'모으',None,u'음',None,u'모음'),
    (u'모으',None,u'으러',None,u'모으러'),
    (u'모으',None,u'을지',None,u'모을지'),
    (u'모으',None,u'을',None,u'모을'),
    (u'모으',None,u'습니다',u'ㅂ니다',u'모읍니다'),
    (u'모으',None,u'소',u'오',u'모으오'),
    (u'모으',None,u'아~어/E-conjunctive',None,u'모아'),
    (u'모으',None,u'아서~어서/E-conjunctive',None,u'모아서'),
    (u'모으',None,u'아~어/E-s-ender',None,u'모아'),
    (u'모으',None,u'아요~어요/E-s-ender',None,u'모아요'),
    (u'모으',None,u'았어요~었어요',None,u'모았어요'),
    (u'모으',None,u'다/E-quote',None,u'모으다'),
    (u'모으',None,u'대/E-quote',None,u'모으대'),
    (u'모으',None,u'으냐고/E-quote',None,u'모으냐고'),

    (u'보',None,u'다',None,u'보다'),
    (u'보',None,u'니',None,u'보니'),
    (u'보',None,u'으니',None,u'보니'),
    (u'보',None,u'세',None,u'보세'),
    (u'보',None,u'으면',None,u'보면'),
    (u'보',None,u'음',None,u'봄'),
    (u'보',None,u'으러',None,u'보러'),
    (u'보',None,u'을지',None,u'볼지'),
    (u'보',None,u'을',None,u'볼'),
    (u'보',None,u'습니다',u'ㅂ니다',u'봅니다'),
    (u'보',None,u'소',u'오',u'보오'),
    (u'보',None,u'아~어/E-conjunctive',None,u'봐,보아'),
    (u'보',None,u'아서~어서/E-conjunctive',None,u'봐서,보아서'),
    (u'보',None,u'아~어/E-s-ender',None,u'봐'),
    (u'보',None,u'아요~어요/E-s-ender',None,u'봐요'),
    (u'보',None,u'았어요~었어요',None,u'봤어요,보았어요'),
    (u'보',None,u'다/E-quote',None,u'보다'),
    (u'보',None,u'대/E-quote',None,u'보대'),
    (u'보',None,u'으냐고/E-quote',None,u'보냐고'),

    (u'주',None,u'다',None,u'주다'),
    (u'주',None,u'니',None,u'주니'),
    (u'주',None,u'으니',None,u'주니'),
    (u'주',None,u'세',None,u'주세'),
    (u'주',None,u'으면',None,u'주면'),
    (u'주',None,u'음',None,u'줌'),
    (u'주',None,u'으러',None,u'주러'),
    (u'주',None,u'을지',None,u'줄지'),
    (u'주',None,u'을',None,u'줄'),
    (u'주',None,u'습니다',u'ㅂ니다',u'줍니다'),
    (u'주',None,u'소',u'오',u'주오'),
    (u'주',None,u'아~어/E-conjunctive',None,u'줘,주어'),
    (u'주',None,u'아서~어서/E-conjunctive',None,u'줘서,주어서'),
    (u'주',None,u'아~어/E-s-ender',None,u'줘'),
    (u'주',None,u'아요~어요/E-s-ender',None,u'줘요'),
    (u'주',None,u'았어요~었어요',None,u'줬어요,주었어요'),
    (u'주',None,u'다/E-quote',None,u'주다'),
    (u'주',None,u'대/E-quote',None,u'주대'),
    (u'주',None,u'으냐고/E-quote',None,u'주냐고'),

    (u'푸',None,u'다',None,u'푸다'),
    (u'푸',None,u'니',None,u'푸니'),
    (u'푸',None,u'으니',None,u'푸니'),
    (u'푸',None,u'세',None,u'푸세'),
    (u'푸',None,u'으면',None,u'푸면'),
    (u'푸',None,u'음',None,u'품'),
    (u'푸',None,u'으러',None,u'푸러'),
    (u'푸',None,u'을지',None,u'풀지'),
    (u'푸',None,u'을',None,u'풀'),
    (u'푸',None,u'습니다',u'ㅂ니다',u'풉니다'),
    (u'푸',None,u'소',u'오',u'푸오'),
    (u'푸',None,u'아~어/E-conjunctive',None,u'퍼'),
    (u'푸',None,u'아서~어서/E-conjunctive',None,u'퍼서'),
    (u'푸',None,u'아~어/E-s-ender',None,u'퍼'),
    (u'푸',None,u'아요~어요/E-s-ender',None,u'퍼요'),
    (u'푸',None,u'았어요~었어요',None,u'펐어요'),
    (u'푸',None,u'다/E-quote',None,u'푸다'),
    (u'푸',None,u'대/E-quote',None,u'푸대'),
    (u'푸',None,u'으냐고/E-quote',None,u'푸냐고'),

    (u'비',None,u'다',None,u'비다'),
    (u'비',None,u'니',None,u'비니'),
    (u'비',None,u'으니',None,u'비니'),
    (u'비',None,u'세',None,u'비세'),
    (u'비',None,u'으면',None,u'비면'),
    (u'비',None,u'음',None,u'빔'),
    (u'비',None,u'으러',None,u'비러'),
    (u'비',None,u'을지',None,u'빌지'),
    (u'비',None,u'을',None,u'빌'),
    (u'비',None,u'습니다',u'ㅂ니다',u'빕니다'),
    (u'비',None,u'소',u'오',u'비오'),
    (u'비',None,u'아~어/E-conjunctive',None,u'비어'),
    (u'비',None,u'아서~어서/E-conjunctive',None,u'비어서'),
    (u'비',None,u'아~어/E-s-ender',None,u'비어'),
    (u'비',None,u'아요~어요/E-s-ender',None,u'비어요'),
    (u'비',None,u'았어요~었어요',None,u'비었어요'),
    (u'비',None,u'다/E-quote',None,u'비다'),
    (u'비',None,u'대/E-quote',None,u'비대'),
    (u'비',None,u'으냐고/E-quote',None,u'비냐고'),

    (u'치',None,u'다',None,u'치다'),
    (u'치',None,u'니',None,u'치니'),
    (u'치',None,u'으니',None,u'치니'),
    (u'치',None,u'세',None,u'치세'),
    (u'치',None,u'으면',None,u'치면'),
    (u'치',None,u'음',None,u'침'),
    (u'치',None,u'으러',None,u'치러'),
    (u'치',None,u'을지',None,u'칠지'),
    (u'치',None,u'을',None,u'칠'),
    (u'치',None,u'습니다',u'ㅂ니다',u'칩니다'),
    (u'치',None,u'소',u'오',u'치오'),
    (u'치',None,u'아~어/E-conjunctive',None,u'쳐,치어'),
    (u'치',None,u'아서~어서/E-conjunctive',None,u'쳐서,치어서'),
    (u'치',None,u'아~어/E-s-ender',None,u'쳐,치어'),
    (u'치',None,u'아요~어요/E-s-ender',None,u'쳐요,치어요'),
    (u'치',None,u'았어요~었어요',None,u'쳤어요,치었어요'),
    (u'치',None,u'다/E-quote',None,u'치다'),
    (u'치',None,u'대/E-quote',None,u'치대'),
    (u'치',None,u'으냐고/E-quote',None,u'치냐고'),

    (u'벌이',None,u'다',None,u'벌이다'),
    (u'벌이',None,u'니',None,u'벌이니'),
    (u'벌이',None,u'으니',None,u'벌이니'),
    (u'벌이',None,u'세',None,u'벌이세'),
    (u'벌이',None,u'으면',None,u'벌이면'),
    (u'벌이',None,u'음',None,u'벌임'),
    (u'벌이',None,u'으러',None,u'벌이러'),
    (u'벌이',None,u'을지',None,u'벌일지'),
    (u'벌이',None,u'을',None,u'벌일'),
    (u'벌이',None,u'습니다',u'ㅂ니다',u'벌입니다'),
    (u'벌이',None,u'소',u'오',u'벌이오'),
    (u'벌이',None,u'아~어/E-conjunctive',None,u'벌여'),
    (u'벌이',None,u'아서~어서/E-conjunctive',None,u'벌여서'),
    (u'벌이',None,u'아~어/E-s-ender',None,u'벌여'),
    (u'벌이',None,u'아요~어요/E-s-ender',None,u'벌여요'),
    (u'벌이',None,u'았어요~었어요',None,u'벌였어요'),
    (u'벌이',None,u'다/E-quote',None,u'벌이다'),
    (u'벌이',None,u'대/E-quote',None,u'벌이대'),
    (u'벌이',None,u'으냐고/E-quote',None,u'벌이냐고'),

    (u'보이',None,u'다',None,u'보이다'),
    (u'보이',None,u'니',None,u'보이니'),
    (u'보이',None,u'으니',None,u'보이니'),
    (u'보이',None,u'세',None,u'보이세'),
    (u'보이',None,u'으면',None,u'보이면'),
    (u'보이',None,u'음',None,u'보임'),
    (u'보이',None,u'으러',None,u'보이러'),
    (u'보이',None,u'을지',None,u'보일지'),
    (u'보이',None,u'을',None,u'보일'),
    (u'보이',None,u'습니다',u'ㅂ니다',u'보입니다'),
    (u'보이',None,u'소',u'오',u'보이오'),
    (u'보이',None,u'아~어/E-conjunctive',None,u'보여'),
    (u'보이',None,u'아서~어서/E-conjunctive',None,u'보여서'),
    (u'보이',None,u'아~어/E-s-ender',None,u'보여'),
    (u'보이',None,u'아요~어요/E-s-ender',None,u'보여요'),
    (u'보이',None,u'았어요~었어요',None,u'보였어요'),
    (u'보이',None,u'다/E-quote',None,u'보이다'),
    (u'보이',None,u'대/E-quote',None,u'보이대'),
    (u'보이',None,u'으냐고/E-quote',None,u'보이냐고'),

    (u'쉬',None,u'다',None,u'쉬다'),
    (u'쉬',None,u'니',None,u'쉬니'),
    (u'쉬',None,u'으니',None,u'쉬니'),
    (u'쉬',None,u'세',None,u'쉬세'),
    (u'쉬',None,u'으면',None,u'쉬면'),
    (u'쉬',None,u'음',None,u'쉼'),
    (u'쉬',None,u'으러',None,u'쉬러'),
    (u'쉬',None,u'을지',None,u'쉴지'),
    (u'쉬',None,u'을',None,u'쉴'),
    (u'쉬',None,u'습니다',u'ㅂ니다',u'쉽니다'),
    (u'쉬',None,u'소',u'오',u'쉬오'),
    (u'쉬',None,u'아~어/E-conjunctive',None,u'쉬어'),
    (u'쉬',None,u'아서~어서/E-conjunctive',None,u'쉬어서'),
    (u'쉬',None,u'아~어/E-s-ender',None,u'쉬어'),
    (u'쉬',None,u'아요~어요/E-s-ender',None,u'쉬어요'),
    (u'쉬',None,u'았어요~었어요',None,u'쉬었어요'),
    (u'쉬',None,u'다/E-quote',None,u'쉬다'),
    (u'쉬',None,u'대/E-quote',None,u'쉬대'),
    (u'쉬',None,u'으냐고/E-quote',None,u'쉬냐고'),

    (u'희',None,u'다',None,u'희다'),
    (u'희',None,u'니',None,u'희니'),
    (u'희',None,u'으니',None,u'희니'),
    (u'희',None,u'세',None,u'희세'),
    (u'희',None,u'으면',None,u'희면'),
    (u'희',None,u'음',None,u'흼'),
    (u'희',None,u'으러',None,u'희러'),
    (u'희',None,u'을지',None,u'흴지'),
    (u'희',None,u'을',None,u'흴'),
    (u'희',None,u'습니다',u'ㅂ니다',u'흽니다'),
    (u'희',None,u'소',u'오',u'희오'),
    (u'희',None,u'아~어/E-conjunctive',None,u'희어'),
    (u'희',None,u'아서~어서/E-conjunctive',None,u'희어서'),
    (u'희',None,u'아~어/E-s-ender',None,u'희어'),
    (u'희',None,u'아요~어요/E-s-ender',None,u'희어요'),
    (u'희',None,u'았어요~었어요',None,u'희었어요'),
    (u'희',None,u'다/E-quote',None,u'희다'),
    (u'희',None,u'대/E-quote',None,u'희대'),
    (u'희',None,u'으냐고/E-quote',None,u'희냐고'),

    (u'되',None,u'다',None,u'되다'),
    (u'되',None,u'니',None,u'되니'),
    (u'되',None,u'으니',None,u'되니'),
    (u'되',None,u'세',None,u'되세'),
    (u'되',None,u'으면',None,u'되면'),
    (u'되',None,u'음',None,u'됨'),
    (u'되',None,u'으러',None,u'되러'),
    (u'되',None,u'을지',None,u'될지'),
    (u'되',None,u'을',None,u'될'),
    (u'되',None,u'습니다',u'ㅂ니다',u'됩니다'),
    (u'되',None,u'소',u'오',u'되오'),
    (u'되',None,u'아~어/E-conjunctive',None,u'돼,되어'),
    (u'되',None,u'아서~어서/E-conjunctive',None,u'돼서,되어서'),
    (u'되',None,u'아~어/E-s-ender',None,u'돼'),
    (u'되',None,u'아요~어요/E-s-ender',None,u'돼요'),
    (u'되',None,u'았어요~었어요',None,u'됐어요,되었어요'),
    (u'되',None,u'다/E-quote',None,u'되다'),
    (u'되',None,u'대/E-quote',None,u'되대'),
    (u'되',None,u'으냐고/E-quote',None,u'되냐고'),

    (u'받',None,u'다',None,u'받다'),
    (u'받',None,u'니',None,u'받니'),
    (u'받',None,u'으니',None,u'받으니'),
    (u'받',None,u'세',None,u'받세'),
    (u'받',None,u'으면',None,u'받으면'),
    (u'받',None,u'음',None,u'받음'),
    (u'받',None,u'으러',None,u'받으러'),
    (u'받',None,u'을지',None,u'받을지'),
    (u'받',None,u'을',None,u'받을'),
    (u'받',None,u'습니다',u'ㅂ니다',u'받습니다'),
    (u'받',None,u'소',u'오',u'받소'),
    (u'받',None,u'아~어/E-conjunctive',None,u'받아'),
    (u'받',None,u'아서~어서/E-conjunctive',None,u'받아서'),
    (u'받',None,u'아~어/E-s-ender',None,u'받아'),
    (u'받',None,u'아요~어요/E-s-ender',None,u'받아요'),
    (u'받',None,u'았어요~었어요',None,u'받았어요'),
    (u'받',None,u'다/E-quote',None,u'받다'),
    (u'받',None,u'대/E-quote',None,u'받대'),
    (u'받',None,u'으냐고/E-quote',None,u'받으냐고'),

    (u'먹',None,u'다',None,u'먹다'),
    (u'먹',None,u'니',None,u'먹니'),
    (u'먹',None,u'으니',None,u'먹으니'),
    (u'먹',None,u'세',None,u'먹세'),
    (u'먹',None,u'으면',None,u'먹으면'),
    (u'먹',None,u'음',None,u'먹음'),
    (u'먹',None,u'으러',None,u'먹으러'),
    (u'먹',None,u'을지',None,u'먹을지'),
    (u'먹',None,u'을',None,u'먹을'),
    (u'먹',None,u'습니다',u'ㅂ니다',u'먹습니다'),
    (u'먹',None,u'소',u'오',u'먹소'),
    (u'먹',None,u'아~어/E-conjunctive',None,u'먹어'),
    (u'먹',None,u'아서~어서/E-conjunctive',None,u'먹어서'),
    (u'먹',None,u'아~어/E-s-ender',None,u'먹어'),
    (u'먹',None,u'아요~어요/E-s-ender',None,u'먹어요'),
    (u'먹',None,u'았어요~었어요',None,u'먹었어요'),
    (u'먹',None,u'다/E-quote',None,u'먹다'),
    (u'먹',None,u'대/E-quote',None,u'먹대'),
    (u'먹',None,u'으냐고/E-quote',None,u'먹으냐고'),

    (u'살',None,u'다',None,u'살다'),
    (u'살',None,u'니',None,u'사니'),
    (u'살',None,u'으니',None,u'사니'),
    (u'살',None,u'세',None,u'사세'),
    (u'살',None,u'으면',None,u'살면'),
    (u'살',None,u'음',None,u'삶'),
    (u'살',None,u'으러',None,u'살러'),
    (u'살',None,u'을지',None,u'살지'),
    (u'살',None,u'을',None,u'살'),
    (u'살',None,u'습니다',u'ㅂ니다',u'삽니다'),
    (u'살',None,u'소',u'오',u'사오'),
    (u'살',None,u'아~어/E-conjunctive',None,u'살아'),
    (u'살',None,u'아서~어서/E-conjunctive',None,u'살아서'),
    (u'살',None,u'아~어/E-s-ender',None,u'살아'),
    (u'살',None,u'아요~어요/E-s-ender',None,u'살아요'),
    (u'살',None,u'았어요~었어요',None,u'살았어요'),
    (u'살',None,u'다/E-quote',None,u'살다'),
    (u'살',None,u'대/E-quote',None,u'살대'),
    (u'살',None,u'으냐고/E-quote',None,u'사냐고'),

    (u'걸',None,u'다',None,u'걸다'),
    (u'걸',None,u'니',None,u'거니'),
    (u'걸',None,u'으니',None,u'거니'),
    (u'걸',None,u'세',None,u'거세'),
    (u'걸',None,u'으면',None,u'걸면'),
    (u'걸',None,u'음',None,u'걺'),
    (u'걸',None,u'으러',None,u'걸러'),
    (u'걸',None,u'을지',None,u'걸지'),
    (u'걸',None,u'을',None,u'걸'),
    (u'걸',None,u'습니다',u'ㅂ니다',u'겁니다'),
    (u'걸',None,u'소',u'오',u'거오'),
    (u'걸',None,u'아~어/E-conjunctive',None,u'걸어'),
    (u'걸',None,u'아서~어서/E-conjunctive',None,u'걸어서'),
    (u'걸',None,u'아~어/E-s-ender',None,u'걸어'),
    (u'걸',None,u'아요~어요/E-s-ender',None,u'걸어요'),
    (u'걸',None,u'았어요~었어요',None,u'걸었어요'),
    (u'걸',None,u'다/E-quote',None,u'걸다'),
    (u'걸',None,u'대/E-quote',None,u'걸대'),
    (u'걸',None,u'으냐고/E-quote',None,u'거냐고'),

    (u'돕','irrb',u'다',None,u'돕다'),
    (u'돕','irrb',u'니',None,u'돕니'),
    (u'돕','irrb',u'으니',None,u'도우니'),
    (u'돕','irrb',u'세',None,u'돕세'),
    (u'돕','irrb',u'으면',None,u'도우면'),
    (u'돕','irrb',u'음',None,u'도움'),
    (u'돕','irrb',u'으러',None,u'도우러'),
    (u'돕','irrb',u'을지',None,u'도울지'),
    (u'돕','irrb',u'을',None,u'도울'),
    (u'돕','irrb',u'습니다',u'ㅂ니다',u'돕습니다'),
    (u'돕','irrb',u'소',u'오',u'돕소'),
    (u'돕','irrb',u'아~어/E-conjunctive',None,u'도와'),
    (u'돕','irrb',u'아서~어서/E-conjunctive',None,u'도와서'),
    (u'돕','irrb',u'아~어/E-s-ender',None,u'도와'),
    (u'돕','irrb',u'아요~어요/E-s-ender',None,u'도와요'),
    (u'돕','irrb',u'았어요~었어요',None,u'도왔어요'),
    (u'돕','irrb',u'다/E-quote',None,u'돕다'),
    (u'돕','irrb',u'대/E-quote',None,u'돕대'),
    (u'돕','irrb',u'으냐고/E-quote',None,u'도우냐고'),

    (u'고맙','irrb',u'다',None,u'고맙다'),
    (u'고맙','irrb',u'니',None,u'고맙니'),
    (u'고맙','irrb',u'으니',None,u'고마우니'),
    (u'고맙','irrb',u'세',None,u'고맙세'),
    (u'고맙','irrb',u'으면',None,u'고마우면'),
    (u'고맙','irrb',u'음',None,u'고마움'),
    (u'고맙','irrb',u'으러',None,u'고마우러'),
    (u'고맙','irrb',u'을지',None,u'고마울지'),
    (u'고맙','irrb',u'을',None,u'고마울'),
    (u'고맙','irrb',u'습니다',u'ㅂ니다',u'고맙습니다'),
    (u'고맙','irrb',u'소',u'오',u'고맙소'),
    (u'고맙','irrb',u'아~어/E-conjunctive',None,u'고마워'),
    (u'고맙','irrb',u'아서~어서/E-conjunctive',None,u'고마워서'),
    (u'고맙','irrb',u'아~어/E-s-ender',None,u'고마워'),
    (u'고맙','irrb',u'아요~어요/E-s-ender',None,u'고마워요'),
    (u'고맙','irrb',u'았어요~었어요',None,u'고마웠어요'),
    (u'고맙','irrb',u'다/E-quote',None,u'고맙다'),
    (u'고맙','irrb',u'대/E-quote',None,u'고맙대'),
    (u'고맙','irrb',u'으냐고/E-quote',None,u'고마우냐고'),

    (u'눕','irrb',u'다',None,u'눕다'),
    (u'눕','irrb',u'니',None,u'눕니'),
    (u'눕','irrb',u'으니',None,u'누우니'),
    (u'눕','irrb',u'세',None,u'눕세'),
    (u'눕','irrb',u'으면',None,u'누우면'),
    (u'눕','irrb',u'음',None,u'누움'),
    (u'눕','irrb',u'으러',None,u'누우러'),
    (u'눕','irrb',u'을지',None,u'누울지'),
    (u'눕','irrb',u'을',None,u'누울'),
    (u'눕','irrb',u'습니다',u'ㅂ니다',u'눕습니다'),
    (u'눕','irrb',u'소',u'오',u'눕소'),
    (u'눕','irrb',u'아~어/E-conjunctive',None,u'누워'),
    (u'눕','irrb',u'아서~어서/E-conjunctive',None,u'누워서'),
    (u'눕','irrb',u'아~어/E-s-ender',None,u'누워'),
    (u'눕','irrb',u'아요~어요/E-s-ender',None,u'누워요'),
    (u'눕','irrb',u'았어요~었어요',None,u'누웠어요'),
    (u'눕','irrb',u'다/E-quote',None,u'눕다'),
    (u'눕','irrb',u'대/E-quote',None,u'눕대'),
    (u'눕','irrb',u'으냐고/E-quote',None,u'누우냐고'),

    (u'뵙','irrb2',u'다',None,u'뵙다'),
    (u'뵙','irrb2',u'니',None,u'뵙니'),
    (u'뵙','irrb2',u'으니',None,u'뵈니'),
    (u'뵙','irrb2',u'세',None,u'뵙세'),
    (u'뵙','irrb2',u'으면',None,u'뵈면'),
    (u'뵙','irrb2',u'음',None,u'뵘'),
    (u'뵙','irrb2',u'으러',None,u'뵈러'),
    (u'뵙','irrb2',u'을지',None,u'뵐지'),
    (u'뵙','irrb2',u'을',None,u'뵐'),
    (u'뵙','irrb2',u'습니다',u'ㅂ니다',u'뵙습니다'),
    (u'뵙','irrb2',u'소',u'오',u'뵙소'),
    (u'뵙','irrb2',u'아~어/E-conjunctive',None,u'봬,뵈어'),
    (u'뵙','irrb2',u'아서~어서/E-conjunctive',None,u'봬서,뵈어서'),
    (u'뵙','irrb2',u'아~어/E-s-ender',None,u'봬'),
    (u'뵙','irrb2',u'아요~어요/E-s-ender',None,u'봬요'),
    (u'뵙','irrb2',u'았어요~었어요',None,u'뵀어요,뵈었어요'),
    (u'뵙','irrb2',u'다/E-quote',None,u'뵙다'),
    (u'뵙','irrb2',u'대/E-quote',None,u'뵙대'),
    (u'뵙','irrb2',u'으냐고/E-quote',None,u'뵈냐고'),

    (u'뵙',None,u'다',None,u'뵙다'),
    (u'뵙',None,u'니',None,u'뵙니'),
    (u'뵙',None,u'으니',None,u'뵈니'),
    (u'뵙',None,u'세',None,u'뵙세'),
    (u'뵙',None,u'으면',None,u'뵈면'),
    (u'뵙',None,u'음',None,u'뵘'),
    (u'뵙',None,u'으러',None,u'뵈러'),
    (u'뵙',None,u'을지',None,u'뵐지'),
    (u'뵙',None,u'을',None,u'뵐'),
    (u'뵙',None,u'습니다',u'ㅂ니다',u'뵙습니다'),
    (u'뵙',None,u'소',u'오',u'뵙소'),
    (u'뵙',None,u'아~어/E-conjunctive',None,u'봬,뵈어'),
    (u'뵙',None,u'아서~어서/E-conjunctive',None,u'봬서,뵈어서'),
    (u'뵙',None,u'아~어/E-s-ender',None,u'봬'),
    (u'뵙',None,u'아요~어요/E-s-ender',None,u'봬요'),
    (u'뵙',None,u'았어요~었어요',None,u'뵀어요,뵈었어요'),
    (u'뵙',None,u'다/E-quote',None,u'뵙다'),
    (u'뵙',None,u'대/E-quote',None,u'뵙대'),
    (u'뵙',None,u'으냐고/E-quote',None,u'뵈냐고'),

    (u'낫','irrs',u'다',None,u'낫다'),
    (u'낫','irrs',u'니',None,u'낫니'),
    (u'낫','irrs',u'으니',None,u'나으니'),
    (u'낫','irrs',u'세',None,u'낫세'),
    (u'낫','irrs',u'으면',None,u'나으면'),
    (u'낫','irrs',u'음',None,u'나음'),
    (u'낫','irrs',u'으러',None,u'나으러'),
    (u'낫','irrs',u'을지',None,u'나을지'),
    (u'낫','irrs',u'을',None,u'나을'),
    (u'낫','irrs',u'습니다',u'ㅂ니다',u'낫습니다'),
    (u'낫','irrs',u'소',u'오',u'낫소'),
    (u'낫','irrs',u'아~어/E-conjunctive',None,u'나아'),
    (u'낫','irrs',u'아서~어서/E-conjunctive',None,u'나아서'),
    (u'낫','irrs',u'아~어/E-s-ender',None,u'나아'),
    (u'낫','irrs',u'아요~어요/E-s-ender',None,u'나아요'),
    (u'낫','irrs',u'았어요~었어요',None,u'나았어요'),
    (u'낫','irrs',u'다/E-quote',None,u'낫다'),
    (u'낫','irrs',u'대/E-quote',None,u'낫대'),
    (u'낫','irrs',u'으냐고/E-quote',None,u'나으냐고'),

    (u'깃','irrs',u'다',None,u'깃다'),
    (u'깃','irrs',u'니',None,u'깃니'),
    (u'깃','irrs',u'으니',None,u'기으니'),
    (u'깃','irrs',u'세',None,u'깃세'),
    (u'깃','irrs',u'으면',None,u'기으면'),
    (u'깃','irrs',u'음',None,u'기음'),
    (u'깃','irrs',u'으러',None,u'기으러'),
    (u'깃','irrs',u'을지',None,u'기을지'),
    (u'깃','irrs',u'을',None,u'기을'),
    (u'깃','irrs',u'습니다',u'ㅂ니다',u'깃습니다'),
    (u'깃','irrs',u'소',u'오',u'깃소'),
    (u'깃','irrs',u'아~어/E-conjunctive',None,u'기어'),
    (u'깃','irrs',u'아서~어서/E-conjunctive',None,u'기어서'),
    (u'깃','irrs',u'아~어/E-s-ender',None,u'기어'),
    (u'깃','irrs',u'아요~어요/E-s-ender',None,u'기어요'),
    (u'깃','irrs',u'았어요~었어요',None,u'기었어요'),
    (u'깃','irrs',u'다/E-quote',None,u'깃다'),
    (u'깃','irrs',u'대/E-quote',None,u'깃대'),
    (u'깃','irrs',u'으냐고/E-quote',None,u'기으냐고'),

    (u'캐닫','irrd',u'다',None,u'캐닫다'),
    (u'캐닫','irrd',u'니',None,u'캐닫니'),
    (u'캐닫','irrd',u'으니',None,u'캐달으니'),
    (u'캐닫','irrd',u'세',None,u'캐닫세'),
    (u'캐닫','irrd',u'으면',None,u'캐달으면'),
    (u'캐닫','irrd',u'음',None,u'캐달음'),
    (u'캐닫','irrd',u'으러',None,u'캐달으러'),
    (u'캐닫','irrd',u'을지',None,u'캐달을지'),
    (u'캐닫','irrd',u'을',None,u'캐달을'),
    (u'캐닫','irrd',u'습니다',u'ㅂ니다',u'캐닫습니다'),
    (u'캐닫','irrd',u'소',u'오',u'캐닫소'),
    (u'캐닫','irrd',u'아~어/E-conjunctive',None,u'캐달아'),
    (u'캐닫','irrd',u'아서~어서/E-conjunctive',None,u'캐달아서'),
    (u'캐닫','irrd',u'아~어/E-s-ender',None,u'캐달아'),
    (u'캐닫','irrd',u'아요~어요/E-s-ender',None,u'캐달아요'),
    (u'캐닫','irrd',u'았어요~었어요',None,u'캐달았어요'),
    (u'캐닫','irrd',u'다/E-quote',None,u'캐닫다'),
    (u'캐닫','irrd',u'대/E-quote',None,u'캐닫대'),
    (u'캐닫','irrd',u'으냐고/E-quote',None,u'캐달으냐고'),

    (u'걷','irrd',u'다',None,u'걷다'),
    (u'걷','irrd',u'니',None,u'걷니'),
    (u'걷','irrd',u'으니',None,u'걸으니'),
    (u'걷','irrd',u'세',None,u'걷세'),
    (u'걷','irrd',u'으면',None,u'걸으면'),
    (u'걷','irrd',u'음',None,u'걸음'),
    (u'걷','irrd',u'으러',None,u'걸으러'),
    (u'걷','irrd',u'을지',None,u'걸을지'),
    (u'걷','irrd',u'을',None,u'걸을'),
    (u'걷','irrd',u'습니다',u'ㅂ니다',u'걷습니다'),
    (u'걷','irrd',u'소',u'오',u'걷소'),
    (u'걷','irrd',u'아~어/E-conjunctive',None,u'걸어'),
    (u'걷','irrd',u'아서~어서/E-conjunctive',None,u'걸어서'),
    (u'걷','irrd',u'아~어/E-s-ender',None,u'걸어'),
    (u'걷','irrd',u'아요~어요/E-s-ender',None,u'걸어요'),
    (u'걷','irrd',u'았어요~었어요',None,u'걸었어요'),
    (u'걷','irrd',u'다/E-quote',None,u'걷다'),
    (u'걷','irrd',u'대/E-quote',None,u'걷대'),
    (u'걷','irrd',u'으냐고/E-quote',None,u'걸으냐고'),

    (u'노랗','irrh',u'다',None,u'노랗다'),
    (u'노랗','irrh',u'니',None,u'노랗니'),
    (u'노랗','irrh',u'으니',None,u'노라니'),
    (u'노랗','irrh',u'세',None,u'노랗세'),
    (u'노랗','irrh',u'으면',None,u'노라면'),
    (u'노랗','irrh',u'음',None,u'노람'),
    (u'노랗','irrh',u'으러',None,u'노라러'),
    (u'노랗','irrh',u'을지',None,u'노랄지'),
    (u'노랗','irrh',u'을',None,u'노랄'),
    (u'노랗','irrh',u'습니다',u'ㅂ니다',u'노랗습니다'),
    (u'노랗','irrh',u'소',u'오',u'노랗소'),
    (u'노랗','irrh',u'아~어/E-conjunctive',None,u'노래'),
    (u'노랗','irrh',u'아서~어서/E-conjunctive',None,u'노래서'),
    (u'노랗','irrh',u'아~어/E-s-ender',None,u'노래'),
    (u'노랗','irrh',u'아요~어요/E-s-ender',None,u'노래요'),
    (u'노랗','irrh',u'았어요~었어요',None,u'노랬어요'),
    (u'노랗','irrh',u'다/E-quote',None,u'노랗다'),
    (u'노랗','irrh',u'대/E-quote',None,u'노랗대'),
    (u'노랗','irrh',u'으냐고/E-quote',None,u'노라냐고'),

    (u'그렇','irrh',u'다',None,u'그렇다'),
    (u'그렇','irrh',u'니',None,u'그렇니'),
    (u'그렇','irrh',u'으니',None,u'그러니'),
    (u'그렇','irrh',u'세',None,u'그렇세'),
    (u'그렇','irrh',u'으면',None,u'그러면'),
    (u'그렇','irrh',u'음',None,u'그럼'),
    (u'그렇','irrh',u'으러',None,u'그러러'),
    (u'그렇','irrh',u'을지',None,u'그럴지'),
    (u'그렇','irrh',u'을',None,u'그럴'),
    (u'그렇','irrh',u'습니다',u'ㅂ니다',u'그렇습니다'),
    (u'그렇','irrh',u'소',u'오',u'그렇소'),
    (u'그렇','irrh',u'아~어/E-conjunctive',None,u'그래'),
    (u'그렇','irrh',u'아서~어서/E-conjunctive',None,u'그래서'),
    (u'그렇','irrh',u'아~어/E-s-ender',None,u'그래'),
    (u'그렇','irrh',u'아요~어요/E-s-ender',None,u'그래요'),
    (u'그렇','irrh',u'았어요~었어요',None,u'그랬어요'),
    (u'그렇','irrh',u'다/E-quote',None,u'그렇다'),
    (u'그렇','irrh',u'대/E-quote',None,u'그렇대'),
    (u'그렇','irrh',u'으냐고/E-quote',None,u'그러냐고'),

    (u'오르','irrlu',u'다',None,u'오르다'),
    (u'오르','irrlu',u'니',None,u'오르니'),
    (u'오르','irrlu',u'으니',None,u'오르니'),
    (u'오르','irrlu',u'세',None,u'오르세'),
    (u'오르','irrlu',u'으면',None,u'오르면'),
    (u'오르','irrlu',u'음',None,u'오름'),
    (u'오르','irrlu',u'으러',None,u'오르러'),
    (u'오르','irrlu',u'을지',None,u'오를지'),
    (u'오르','irrlu',u'을',None,u'오를'),
    (u'오르','irrlu',u'습니다',u'ㅂ니다',u'오릅니다'),
    (u'오르','irrlu',u'소',u'오',u'오르오'),
    (u'오르','irrlu',u'아~어/E-conjunctive',None,u'올라'),
    (u'오르','irrlu',u'아서~어서/E-conjunctive',None,u'올라서'),
    (u'오르','irrlu',u'아~어/E-s-ender',None,u'올라'),
    (u'오르','irrlu',u'아요~어요/E-s-ender',None,u'올라요'),
    (u'오르','irrlu',u'았어요~었어요',None,u'올랐어요'),
    (u'오르','irrlu',u'다/E-quote',None,u'오르다'),
    (u'오르','irrlu',u'대/E-quote',None,u'오르대'),
    (u'오르','irrlu',u'으냐고/E-quote',None,u'오르냐고'),

    (u'부르','irrlu',u'다',None,u'부르다'),
    (u'부르','irrlu',u'니',None,u'부르니'),
    (u'부르','irrlu',u'으니',None,u'부르니'),
    (u'부르','irrlu',u'세',None,u'부르세'),
    (u'부르','irrlu',u'으면',None,u'부르면'),
    (u'부르','irrlu',u'음',None,u'부름'),
    (u'부르','irrlu',u'으러',None,u'부르러'),
    (u'부르','irrlu',u'을지',None,u'부를지'),
    (u'부르','irrlu',u'을',None,u'부를'),
    (u'부르','irrlu',u'습니다',u'ㅂ니다',u'부릅니다'),
    (u'부르','irrlu',u'소',u'오',u'부르오'),
    (u'부르','irrlu',u'아~어/E-conjunctive',None,u'불러'),
    (u'부르','irrlu',u'아서~어서/E-conjunctive',None,u'불러서'),
    (u'부르','irrlu',u'아~어/E-s-ender',None,u'불러'),
    (u'부르','irrlu',u'아요~어요/E-s-ender',None,u'불러요'),
    (u'부르','irrlu',u'았어요~었어요',None,u'불렀어요'),
    (u'부르','irrlu',u'다/E-quote',None,u'부르다'),
    (u'부르','irrlu',u'대/E-quote',None,u'부르대'),
    (u'부르','irrlu',u'으냐고/E-quote',None,u'부르냐고'),

    (u'이르','irrle',u'다',None,u'이르다'),
    (u'이르','irrle',u'니',None,u'이르니'),
    (u'이르','irrle',u'으니',None,u'이르니'),
    (u'이르','irrle',u'세',None,u'이르세'),
    (u'이르','irrle',u'으면',None,u'이르면'),
    (u'이르','irrle',u'음',None,u'이름'),
    (u'이르','irrle',u'으러',None,u'이르러'),
    (u'이르','irrle',u'을지',None,u'이를지'),
    (u'이르','irrle',u'을',None,u'이를'),
    (u'이르','irrle',u'습니다',u'ㅂ니다',u'이릅니다'),
    (u'이르','irrle',u'소',u'오',u'이르오'),
    (u'이르','irrle',u'아~어/E-conjunctive',None,u'이르러'),
    (u'이르','irrle',u'아서~어서/E-conjunctive',None,u'이르러서'),
    (u'이르','irrle',u'아~어/E-s-ender',None,u'이르러'),
    (u'이르','irrle',u'아요~어요/E-s-ender',None,u'이르러요'),
    (u'이르','irrle',u'았어요~었어요',None,u'이르렀어요'),
    (u'이르','irrle',u'다/E-quote',None,u'이르다'),
    (u'이르','irrle',u'대/E-quote',None,u'이르대'),
    (u'이르','irrle',u'으냐고/E-quote',None,u'이르냐고'),

    (u'사람','cop',u'다',None,u'사람이다'),
    (u'사람','cop',u'니',None,u'사람이니'),
    (u'사람','cop',u'으니',None,u'사람이니'),
    (u'사람','cop',u'세',None,u'사람이세'),
    (u'사람','cop',u'으면',None,u'사람이면'),
    (u'사람','cop',u'음',None,u'사람임'),
    (u'사람','cop',u'으러',None,u'사람이러'),
    (u'사람','cop',u'을지',None,u'사람일지'),
    (u'사람','cop',u'을',None,u'사람일'),
    (u'사람','cop',u'습니다',u'ㅂ니다',u'사람입니다'),
    (u'사람','cop',u'소',u'오',u'사람이오'),
    (u'사람','cop',u'아~어/E-conjunctive',None,u'사람이라'),
    (u'사람','cop',u'아서~어서/E-conjunctive',None,u'사람이라서'),
    (u'사람','cop',u'아~어/E-s-ender',None,u'사람이야'),
    (u'사람','cop',u'아요~어요/E-s-ender',None,u'사람이에요'),
    (u'사람','cop',u'았어요~었어요',None,u'사람이었어요'),
    (u'사람','cop',u'다/E-quote',None,u'사람이라'),
    (u'사람','cop',u'대/E-quote',None,u'사람이래'),
    (u'사람','cop',u'으냐고/E-quote',None,u'사람이냐고'),

    (u'의사','cop',u'다',None,u'의사다'),
    (u'의사','cop',u'니',None,u'의사니'),
    (u'의사','cop',u'으니',None,u'의사니'),
    (u'의사','cop',u'세',None,u'의사세'),
    (u'의사','cop',u'으면',None,u'의사면'),
    (u'의사','cop',u'음',None,u'의삼'),
    (u'의사','cop',u'으러',None,u'의사러'),
    (u'의사','cop',u'을지',None,u'의살지'),
    (u'의사','cop',u'을',None,u'의살'),
    (u'의사','cop',u'습니다',u'ㅂ니다',u'의사입니다'),
    (u'의사','cop',u'소',u'오',u'의사오'),
    (u'의사','cop',u'아~어/E-conjunctive',None,u'의사라'),
    (u'의사','cop',u'아서~어서/E-conjunctive',None,u'의사라서'),
    (u'의사','cop',u'아~어/E-s-ender',None,u'의사야'),
    (u'의사','cop',u'아요~어요/E-s-ender',None,u'의사예요'),
    (u'의사','cop',u'았어요~었어요',None,u'의사였어요'),
    (u'의사','cop',u'다/E-quote',None,u'의사라'),
    (u'의사','cop',u'대/E-quote',None,u'의사래'),
    (u'의사','cop',u'으냐고/E-quote',None,u'의사냐고'),

    (u'것','cop',u'다',None,u'것이다'),
    (u'것','cop',u'니',None,u'것이니'),
    (u'것','cop',u'으니',None,u'것이니'),
    (u'것','cop',u'세',None,u'것이세'),
    (u'것','cop',u'으면',None,u'것이면'),
    (u'것','cop',u'음',None,u'것임'),
    (u'것','cop',u'으러',None,u'것이러'),
    (u'것','cop',u'을지',None,u'것일지'),
    (u'것','cop',u'을',None,u'것일'),
    (u'것','cop',u'습니다',u'ㅂ니다',u'것입니다'),
    (u'것','cop',u'소',u'오',u'것이오'),
    (u'것','cop',u'아~어/E-conjunctive',None,u'것이라'),
    (u'것','cop',u'아서~어서/E-conjunctive',None,u'것이라서'),
    (u'것','cop',u'아~어/E-s-ender',None,u'것이야'),
    (u'것','cop',u'아요~어요/E-s-ender',None,u'것이에요'),
    (u'것','cop',u'았어요~었어요',None,u'것이었어요'),
    (u'것','cop',u'다/E-quote',None,u'것이라'),
    (u'것','cop',u'대/E-quote',None,u'것이래'),
    (u'것','cop',u'으냐고/E-quote',None,u'것이냐고'),

    (u'거','cop',u'다',None,u'거다'),
    (u'거','cop',u'니',None,u'거니'),
    (u'거','cop',u'으니',None,u'거니'),
    (u'거','cop',u'세',None,u'거세'),
    (u'거','cop',u'으면',None,u'거면'),
    (u'거','cop',u'음',None,u'검'),
    (u'거','cop',u'으러',None,u'거러'),
    (u'거','cop',u'을지',None,u'걸지'),
    (u'거','cop',u'을',None,u'걸'),
    (u'거','cop',u'습니다',u'ㅂ니다',u'겁니다'),
    (u'거','cop',u'소',u'오',u'거오'),
    (u'거','cop',u'아~어/E-conjunctive',None,u'거라'),
    (u'거','cop',u'아서~어서/E-conjunctive',None,u'거라서'),
    (u'거','cop',u'아~어/E-s-ender',None,u'거야'),
    (u'거','cop',u'아요~어요/E-s-ender',None,u'거예요'),
    (u'거','cop',u'았어요~었어요',None,u'거였어요'),
    (u'거','cop',u'다/E-quote',None,u'거라'),
    (u'거','cop',u'대/E-quote',None,u'거래'),
    (u'거','cop',u'으냐고/E-quote',None,u'거냐고'),

    (u'아니','cop',u'다',None,u'아니다'),
    (u'아니','cop',u'니',None,u'아니니'),
    (u'아니','cop',u'으니',None,u'아니니'),
    (u'아니','cop',u'세',None,u'아니세'),
    (u'아니','cop',u'으면',None,u'아니면'),
    (u'아니','cop',u'음',None,u'아님'),
    (u'아니','cop',u'으러',None,u'아니러'),
    (u'아니','cop',u'을지',None,u'아닐지'),
    (u'아니','cop',u'을',None,u'아닐'),
    (u'아니','cop',u'습니다',u'ㅂ니다',u'아닙니다'),
    (u'아니','cop',u'소',u'오',u'아니오'),
    (u'아니','cop',u'아~어/E-conjunctive',None,u'아니라'),
    (u'아니','cop',u'아서~어서/E-conjunctive',None,u'아니라서'),
    (u'아니','cop',u'아~어/E-s-ender',None,u'아니야'),
    (u'아니','cop',u'아요~어요/E-s-ender',None,u'아니예요'),
    (u'아니','cop',u'았어요~었어요',None,u'아니였어요'),
    (u'아니','cop',u'다/E-quote',None,u'아니라'),
    (u'아니','cop',u'대/E-quote',None,u'아니래'),
    (u'아니','cop',u'으냐고/E-quote',None,u'아니냐고'),
    ]
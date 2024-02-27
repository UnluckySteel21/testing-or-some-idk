from ..trtrr import shorten

def test_shorten():
    assert shorten("My Uncle John was an avid fisherman, one who loved to share his passion with anyone willing to join him. However, he wasn't exactly known for being a natural talent in the sport. One memorable fishing trip comes to mind when I joined him at the lake. John, fully equipped with his trusty fishing hat and rod, managed to cast his line further than he'd ever achieved before – only to hook his own hat, which he didn't realize until he reeled it in with pride. We all had a good chuckle, and I'm sure he's already planning a fishing trip in the great beyond, complete with the same lucky hat.") == "My ncl Jhn ws n vd fshrmn, n wh lvd t shr hs pssn wth nyn wllng t jn hm. Hwvr, h wsn't xctly knwn fr bng  ntrl tlnt n th sprt. n mmrbl fshng trp cms t mnd whn  jnd hm t th lk. Jhn, flly qppd wth hs trsty fshng ht nd rd, mngd t cst hs ln frthr thn h'd vr chvd bfr – nly t hk hs wn ht, whch h ddn't rlz ntl h rld t n wth prd. W ll hd  gd chckl, nd 'm sr h's lrdy plnnng  fshng trp n th grt bynd, cmplt wth th sm lcky ht."
    assert shorten("Q: Why do Jewish men get circumcised? A: Because Jewish women won't touch anything unless it's 200 percent off.") == "Q: Why d Jwsh mn gt crcmcsd? : Bcs Jwsh wmn wn't tch nythng nlss t's 200 prcnt ff."
    assert shorten("What's Mexicos National sport? Cross Country.") == "Wht's Mxcs Ntnl sprt? Crss Cntry."
    assert shorten("") == ""
    assert shorten("Why did the Jews roam the desert for 400 years? Someone lost a quarter.") == "Why dd th Jws rm th dsrt fr 400 yrs? Smn lst  qrtr."
    assert shorten("What's the difference between a dead baby and a Styrofoam cup? A dead baby doesn't harm the atmosphere when you burn it.") == "Wht's th dffrnc btwn  dd bby nd  Styrfm cp?  dd bby dsn't hrm th tmsphr whn y brn t."
    assert shorten("What has more brains than a dead baby? The wall behind it.") == "Wht hs mr brns thn  dd bby? Th wll bhnd t."
    assert shorten("Yo momma so ugly she threw a boomerang and it refused to come back.")  == "Y mmm s gly sh thrw  bmrng nd t rfsd t cm bck."
    assert shorten("Yo Momma So Fat The Only Letters She Knows In The Alphabet Are K.F.C!") == "Y Mmm S Ft Th nly Lttrs Sh Knws n Th lphbt r K.F.C!"
    assert shorten("Q: What can strike a blonde without her even knowing it? A: A thought.") == "Q: Wht cn strk  blnd wtht hr vn knwng t? :  thght."

test_shorten()
import math
from lib import *

FOOT_OK = ('Original verses of Pt. Daulatram, checked line by line against a scanned Digambar edition (Chhahdhala Pravachan). Spelling of Braj words (e.g. ैं / ें) varies between printings. Meanings and explanations are written for this site. Please proofread against your own copy.',
           'पं. दौलतराम जी के मूल पद, एक स्कैन किए गए दिगंबर संस्करण (छहढाला प्रवचन) से पंक्ति-दर-पंक्ति मिलान किए गए हैं। ब्रज शब्दों की वर्तनी (जैसे ैं / ें) छपाइयों में भिन्न मिलती है। अर्थ और व्याख्या इस साइट के लिए लिखी गई हैं। कृपया अपने ग्रंथ से मिलान कर लें।')

# ---------- diagram: samsara wheel ----------
def wheel():
    nodes = [
        ('Nigod / Ekendriya', 'निगोद / एकेन्द्रिय', 'acc'),
        ('Tras: 2–4 senses', 'त्रस: दो से चार इंद्रिय', 'gold'),
        ('Tiryanch (5 senses)', 'तिर्यंच (पंचेन्द्रिय)', 'gold'),
        ('Nark (hell)', 'नरक', 'red'),
        ('Manushya (human)', 'मनुष्य', 'green'),
        ('Dev (celestial)', 'देव', 'teal'),
    ]
    cx, cy, R, w, h = 330, 190, 135, 150, 44
    pts = []
    for i in range(6):
        a = -math.pi / 2 + i * math.pi / 3
        pts.append((cx + R * 1.55 * math.cos(a), cy + R * math.sin(a)))
    s = [f'<svg viewBox="0 0 660 380" width="660" role="img" aria-label="Samsara wheel">',
         '<defs><marker id="wa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" class="ah"/></marker></defs>']
    for i in range(6):
        x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % 6]
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        # shorten to leave the boxes
        def edge(ux, uy):
            tx = (w / 2) / abs(ux) if ux else 1e9
            ty = (h / 2) / abs(uy) if uy else 1e9
            return min(tx, ty) + 6
        e = edge(ux, uy)
        s.append(f'<path class="ln" marker-end="url(#wa)" d="M{x1+ux*e:.0f} {y1+uy*e:.0f}L{x2-ux*e:.0f} {y2-uy*e:.0f}"/>')
    for (x, y), (en, hi, c) in zip(pts, nodes):
        s.append(f'<rect class="nd {c}" x="{x-w/2:.0f}" y="{y-h/2:.0f}" width="{w}" height="{h}" rx="12"/>')
        s.append(svgtext(f'{x:.0f}', f'{y+5:.0f}', en, hi, 't'))
    s.append(svgtext(cx, cy - 4, 'Samsara', 'संसार', 't'))
    s.append(svgtext(cx, cy + 16, 'endless cycle without samyagdarshan', 'सम्यग्दर्शन बिना अंतहीन चक्र', 't2'))
    s.append('</svg>')
    return '<div class="svgbox">' + ''.join(s) + '</div>'

DUKH_TABLE = table(
    [b('Gati', 'गति'), b('Main sufferings', 'मुख्य दुःख'), b('Verses', 'पद')],
    [[b('Nigod / Ekendriya', 'निगोद / एकेन्द्रिय'), b('Infinite time in one-sensed bodies; 18 births and deaths in one breath', 'अनंत काल एकेन्द्रिय शरीर में; एक श्वास में अठारह बार जन्म-मरण'), '3–4'],
     [b('Tiryanch (animals)', 'तिर्यंच (पशु)'), b('Crushed by the strong, cutting and piercing, hunger, thirst, burdens, cold and heat', 'सबल द्वारा खाया जाना, छेदन-भेदन, भूख-प्यास, बोझ, शीत-ताप'), '5–7'],
     [b('Nark (hell)', 'नरक'), b('Fearful ground, rivers of pus, sword-leaf trees, extreme cold and heat, body cut to bits, unquenchable hunger and thirst', 'भयानक भूमि, पीब की नदी, असिपत्र वृक्ष, अति शीत-उष्ण, देह के खंड, अतृप्त भूख-प्यास'), '8–12'],
     [b('Manushya (human)', 'मनुष्य'), b('Confinement in the womb, ignorant childhood, lust in youth, helpless old age', 'गर्भवास, अज्ञानी बचपन, यौवन में विषयासक्ति, लाचार बुढ़ापा'), '13–14'],
     [b('Dev (celestial)', 'देव'), b('Burning desire for pleasures, lament at death, and rebirth as a one-sensed being', 'विषय-चाह की दावानल, मरण का विलाप, फिर एकेन्द्रिय में जन्म'), '15–16']])

DHAL1_UNITS = {}
def u(no, text, mean, ex, terms=None, title=None, v='ok', kind='hi', note=None):
    d = dict(no=no, text=text, mean=mean, ex=ex, v=v, kind=kind)
    if terms: d['terms'] = terms
    if title: d['title'] = title
    if note: d['note'] = note
    return d

# ======================= DHAL 1 =======================
d1_m = u('मं', "तीन भुवन में सार, वीतराग-विज्ञानता।\nशिवस्वरूप शिवकार, नमहुँ त्रियोग सम्हारिकैं॥",
 ('Of all that exists in the three worlds, the essence is Vitaraga-Vijnanata: freedom from attachment and aversion together with perfect knowledge (Kevalajnana). It is itself the nature of liberation and also the cause of liberation. I bow to it with mind, speech and body, held steady.',
  'तीनों लोकों में सार वस्तु है वीतरागता सहित विज्ञानता, अर्थात् राग-द्वेष का अभाव और पूर्ण (केवल) ज्ञान। वही मोक्ष का स्वरूप है और मोक्ष का कारण भी। मन, वचन और काया को स्थिर करके मैं उसे नमस्कार करता हूँ।'),
 ('This opening couplet is the mangalacharan, in the metre called Soratha. The poet bows not to a person but to a state: the pure state of Vitaraga-Vijnana, found in the Arihant and Siddha. "Shiv-svarup" says it is of the nature of liberation; "Shiv-kar" says it makes others liberated, because it is the path. "Triyog samharikain" means gathering up the three yogas (mind, speech, body) before bowing.',
  'यह आरंभिक पद मंगलाचरण है, सोरठा छंद में। कवि किसी व्यक्ति को नहीं, एक अवस्था को नमन करते हैं: अरिहंत और सिद्ध में प्रकट वीतराग-विज्ञान की शुद्ध अवस्था को। "शिवस्वरूप" यानी जो स्वयं मोक्ष-स्वरूप है; "शिवकार" यानी जो मोक्ष कराने वाली है, क्योंकि वही मोक्षमार्ग है। "त्रियोग सम्हारिकैं" का अर्थ है मन-वचन-काया इन तीन योगों को समेटकर नमन करना।'),
 terms=[('वीतराग', 'free from attachment and aversion', 'राग-द्वेष रहित'), ('विज्ञानता', 'special (perfect) knowledge', 'विशेष अर्थात् पूर्ण ज्ञान'), ('शिव', 'liberation', 'मोक्ष')],
 title=('Mangalacharan', 'मंगलाचरण'))
d1 = [d1_m]
d1.append(u('1', "जे त्रिभुवन में जीव अनन्त, सुख चाहैं दुखतैं भयवन्त।\nतातैं दुखहारी सुखकार, कहैं सीख गुरु करुणा धार॥",
 ('The infinite souls in the three worlds all want happiness and are afraid of suffering. So the Guru, filled with compassion, gives teaching that removes suffering and brings happiness.',
  'तीनों लोकों में अनंत जीव हैं; सब सुख चाहते हैं और दुःख से डरते हैं। इसलिए करुणावान गुरु दुःख दूर करने वाली और सुख देने वाली शिक्षा देते हैं।'),
 ('This verse states the purpose of the whole book: every living being, from the smallest nigod to a heavenly god, wants happiness and fears pain. But most do not know what true happiness is or where pain comes from. Seeing this, the Digambar Acharya (Guru) teaches with compassion, not for his own benefit. The poet will now give that teaching in the six Dhals.',
  'यह पद पूरे ग्रंथ का प्रयोजन बताता है: निगोद से लेकर देव तक हर जीव सुख चाहता है और दुःख से डरता है। परंतु अधिकांश जीव नहीं जानते कि सच्चा सुख क्या है और दुःख कहाँ से आता है। यह देखकर निर्ग्रंथ आचार्य (गुरु) करुणा से उपदेश देते हैं, अपने लाभ के लिए नहीं। वही उपदेश कवि अब छह ढालों में कहेंगे।'),
 terms=[('त्रिभुवन', 'the three worlds (urdhva, madhya, adho)', 'तीन लोक'), ('सीख', 'teaching, lesson', 'शिक्षा')],
 title=('Purpose of the book', 'ग्रंथ का प्रयोजन')))
d1.append(u('2', "ताहि सुनो भवि मन थिर आन, जो चाहो अपनो कल्यान।\nमोह महामद पियो अनादि, भूल आपको भरमत बादि॥",
 ('O Bhavya (soul capable of liberation), listen to it with a steady mind, if you want your own welfare. From beginningless time the soul has drunk the great intoxicant of delusion (moha); forgetting its own self, it wanders in vain.',
  'हे भव्य जीव! यदि तुम अपना कल्याण चाहते हो तो मन को स्थिर करके उसे सुनो। अनादि काल से आत्मा ने मोह रूपी महान मदिरा पी रखी है; अपने आप को भूलकर वह व्यर्थ ही भटक रही है।'),
 ('The cause of wandering is named at once: moha (Mohaniya karma, the king of the eight karmas, see the Karma Siddhant page). Like a drunk person who forgets who he is, the soul forgets its own nature as a knower and takes the body, family and wealth to be itself. "Badi" means in vain: all this travel has brought no benefit. "Bhavya" shows the audience: the one who can attain liberation and wants it.',
  'भटकने का कारण तुरंत बता दिया: मोह (मोहनीय कर्म, जो आठ कर्मों का राजा है, देखें कर्म सिद्धांत पृष्ठ)। जैसे शराबी अपने को भूल जाता है, वैसे ही आत्मा अपने ज्ञायक स्वभाव को भूलकर शरीर, परिवार और धन को ही अपना मान लेती है। "बादि" यानी व्यर्थ: इस सारे भ्रमण से कोई लाभ नहीं हुआ। "भवि" से श्रोता का परिचय मिलता है: जो मोक्ष पाने योग्य है और उसे चाहता है।'),
 terms=[('भवि', 'bhavya: capable of liberation', 'मोक्ष के योग्य जीव'), ('महामद', 'great intoxicant', 'भारी नशा'), ('बादि', 'in vain', 'व्यर्थ')],
 title=('Why the soul wanders', 'भटकने का कारण')))
d1.append(u('3', "तास भ्रमन की है बहु कथा, पै कछु कहूँ कही मुनि यथा।\nकाल अनन्त निगोद मँझार, बीत्यो एकेन्द्री तन धार॥",
 ('The story of that wandering is long, but I will tell a little, as the sages have told it. The soul spent infinite time in Nigod, taking a one-sensed body.',
  'उस भ्रमण की कथा बहुत लंबी है, फिर भी जैसी मुनियों ने कही है वैसी थोड़ी-सी मैं कहता हूँ। आत्मा ने एकेन्द्रिय शरीर धारण कर निगोद में अनंत काल बिताया।'),
 ('"Kahi muni yatha" tells us the authority: the poet is not inventing, he repeats what the Acharyas taught in the Agam. Nigod is the lowest state of life: sadharan vanaspati, where infinite souls share one body, with only the sense of touch. Souls in nigod are of two kinds: nitya-nigod (never yet came out) and itara-nigod (came out and went back). The first stop of the soul’s journey is therefore the very bottom.',
  '"कही मुनि यथा" से प्रमाण का संकेत मिलता है: कवि अपनी ओर से नहीं कह रहे, वही कह रहे हैं जो आचार्यों ने आगम में कहा। निगोद जीवन की सबसे निम्न अवस्था है: साधारण वनस्पति, जहाँ अनंत जीव एक ही शरीर के स्वामी होते हैं और केवल स्पर्श इंद्रिय होती है। निगोद जीव दो प्रकार के हैं: नित्य-निगोद (जो कभी निकले ही नहीं) और इतर-निगोद (निकलकर लौट आए)। इस प्रकार आत्मा की यात्रा का पहला पड़ाव सबसे नीचे का है।'),
 terms=[('निगोद', 'nigod: sadharan vanaspati, infinite souls in one body', 'साधारण वनस्पति, एक शरीर में अनंत जीव'), ('एकेन्द्री', 'one-sensed (touch only)', 'केवल स्पर्श इंद्रिय वाला')],
 title=('Nigod', 'निगोद')))
d1.append(u('4', "एक श्वास में अठदस बार, जन्म्यो मरयो भरयो दुख भार।\nनिकसि भूमि जल पावक भयो, पवन प्रत्येक वनस्पति थयो॥",
 ('In a single breath the soul was born and died eighteen times, bearing a heavy load of suffering. Coming out of Nigod it became earth, water, fire, air, or Pratyek-vanaspati (a plant with one soul per body).',
  'एक श्वास में यह जीव अठारह बार जन्मा और मरा, दुःख का भारी बोझ सहा। निगोद से निकलकर यह पृथ्वी, जल, अग्नि, वायु या प्रत्येक वनस्पति बना।'),
 ('Two ideas in one verse. First, the shortness of the life in nigod: eighteen births and deaths in one breath. Second, the five one-sensed bodies, the Sthavar kaya: earth, water, fire, air and plant. Pratyek vanaspati has one soul in each body, unlike nigod (sadharan). Getting out of nigod is itself a rare event: the Agam says that for every soul that attains liberation, an equal number leave nigod.',
  'एक ही पद में दो बातें। पहली, निगोद में आयु की अल्पता: एक श्वास में अठारह जन्म-मरण। दूसरी, पाँच प्रकार के एकेन्द्रिय (स्थावर काय): पृथ्वी, जल, अग्नि, वायु और वनस्पति। प्रत्येक वनस्पति में एक शरीर का एक ही जीव स्वामी होता है, जबकि निगोद (साधारण) में अनंत। निगोद से निकलना ही दुर्लभ है: आगम कहता है कि जितने जीव मोक्ष जाते हैं, उतने ही निगोद से बाहर निकलते हैं।'),
 terms=[('अठदस', 'eighteen', 'अठारह'), ('स्थावर', 'immobile one-sensed beings', 'स्थिर एकेन्द्रिय जीव'), ('प्रत्येक वनस्पति', 'plant, one soul per body', 'एक शरीर में एक जीव')],
 title=('Eighteen births in a breath', 'एक श्वास में अठारह बार')))
d1.append(u('5', "दुर्लभ लहि ज्यों चिन्तामणि, त्यों पर्याय लही त्रसतणी।\nलट पिपील अलि आदि शरीर, धर धर मरयो सही बहु पीर॥",
 ('Just as a Chintamani jewel is hard to get, so the Tras body (a mobile being) was gained with great difficulty. There it took the bodies of larvae, ants, bees and the like, and died again and again in great pain.',
  'जैसे चिंतामणि रत्न का मिलना कठिन है, वैसे ही त्रस पर्याय का मिलना भी बहुत कठिन था। उसमें लट, चींटी, भौंरा आदि के शरीर धर-धरकर बार-बार मरा और बहुत पीड़ा सही।'),
 ('Tras means a being with two to five senses. The poet compares the rarity of reaching Tras with a Chintamani: out of the huge number of one-sensed souls, only a few come up. Lat (earthworm/larva) is two-sensed, Pipil (ant) is three-sensed, Ali (bee) is four-sensed. Even here there is no peace, since these small beings are crushed and killed easily.',
  'त्रस यानी दो से पाँच इंद्रियों वाला जीव। कवि ने त्रस पर्याय की दुर्लभता चिंतामणि से समझाई: असंख्य एकेन्द्रिय जीवों में से थोड़े ही ऊपर आते हैं। लट (इल्ली) दो इंद्रिय, पिपील (चींटी) तीन इंद्रिय, अलि (भौंरा) चार इंद्रिय है। यहाँ भी शांति नहीं, क्योंकि ऐसे छोटे जीव आसानी से कुचल जाते और मर जाते हैं।'),
 terms=[('त्रस', 'mobile beings (2 to 5 senses)', 'दो से पाँच इंद्रिय वाले जीव'), ('लट', 'two-sensed larva/worm', 'दो इंद्रिय'), ('पिपील', 'three-sensed ant', 'तीन इंद्रिय'), ('अलि', 'four-sensed bee', 'चार इंद्रिय')],
 title=('Gaining Tras body', 'त्रस पर्याय')))
d1.append(u('6', "कबहूँ पंचेन्द्रिय पशु भयो, मन बिन निपट अज्ञानी थयो।\nसिंहादिक सैनी ह्वै क्रूर, निबल पशु हति खाये भूर॥",
 ('Sometimes the soul became a five-sensed animal and, being without a mind, was utterly ignorant. Sometimes it became a mindful (saini) animal such as a lion, cruel, and killed and ate many weak animals.',
  'कभी यह पंचेन्द्रिय पशु बना, तब मन न होने से बिल्कुल अज्ञानी रहा। कभी सिंह आदि सैनी (मन सहित) पशु होकर क्रूर बना और बहुत-से निर्बल पशुओं को मारकर खाया।'),
 ('Five-sensed animals are of two kinds: Asanji (without mind, e.g. some fish, snakes born from eggs) and Sanji (with mind). Without a mind the animal cannot think of good or bad. With a mind but without right belief, it uses the mind for cruelty (himsa), and so binds fresh karma which leads to hell. The verse warns that intelligence alone is not enough: it is the use of it that matters.',
  'पंचेन्द्रिय पशु दो प्रकार के हैं: असैनी (मन रहित) और सैनी (मन सहित)। मन के बिना पशु भले-बुरे का विचार नहीं कर सकता। मन हो पर सम्यक् श्रद्धा न हो तो मन का उपयोग हिंसा में होता है और नया कर्मबंध होता है जो नरक तक ले जाता है। यह पद सिखाता है कि केवल बुद्धि पर्याप्त नहीं, उसका उपयोग महत्त्वपूर्ण है।'),
 terms=[('सैनी', 'sanji: having a mind', 'मन सहित'), ('असैनी', 'asanji: without a mind', 'मन रहित')],
 title=('Animals: with and without mind', 'पशु: मन सहित और रहित')))
d1.append(u('7', "कबहूँ आप भयो बलहीन, सबलनि करि खायो अति दीन।\nछेदन भेदन भूख पियास, भार-वहन हिम आतप त्रास॥",
 ('At other times the soul itself was weak and was eaten by the strong, helpless and miserable. It suffered cutting and piercing, hunger and thirst, carrying burdens, and the fear of cold and heat.',
  'कभी यह स्वयं निर्बल हुआ तो बलवानों ने इसे अत्यंत दीन अवस्था में खा लिया। छेदन-भेदन, भूख-प्यास, बोझ ढोना, शीत और गर्मी का कष्ट इसने सहा।'),
 ('The suffering of the Tiryanch gati is listed by name: chhedan (cutting), bhedan (piercing), bhookh-piyas (hunger and thirst), bhar-vahan (carrying loads), him (cold), atap (heat). A weak animal fears the strong, a strong animal kills the weak: in both cases there is dukkha. The poet wants the listener to feel that this is not a distant story: this was our own past.',
  'तिर्यंच गति के दुःख गिनाए गए हैं: छेदन, भेदन, भूख-प्यास, भार-वहन, ठंड और गर्मी। निर्बल पशु बलवान से डरता है और बलवान निर्बल को मारता है: दोनों में दुःख है। कवि चाहते हैं कि श्रोता अनुभव करे कि यह कोई दूर की कथा नहीं, हमारा अपना अतीत है।'),
 title=('Sufferings of animals', 'तिर्यंच के दुःख')))
d1.append(u('8', "बध बंधन आदिक दुख घने, कोटि जीभतैं जात न भने।\nअति संक्लेश भावतैं मरयो, घोर श्वभ्रसागर में परयो॥",
 ('There were countless sufferings such as being killed and tied up, too many to tell even with a crore of tongues. Dying with extremely harsh and distressed thoughts (sanklesh bhav), the soul fell into the terrible sea of hell.',
  'वध, बंधन आदि अनेक दुःख इतने हैं कि करोड़ जीभों से भी नहीं कहे जा सकते। अत्यंत संक्लेश भाव से मरकर यह घोर नरक रूपी समुद्र में जा गिरा।'),
 ('The bridge from animal life to hell: it is the state of mind at death. Intense cruelty and sanklesh (distressed, violent thoughts) bind Narak-ayu (hell-life karma). This links to the Karma Siddhant: Ayu karma for hell is bound by heavy arambha and parigraha. "Shvabhra" is a name for hell, and "sagar" shows how vast and hard to cross it is.',
  'पशु-जीवन से नरक तक का पुल है मरण के समय के भाव। तीव्र क्रूरता और संक्लेश (दुःखी, हिंसक भाव) से नरक-आयु का बंध होता है। यह कर्म सिद्धांत से जुड़ता है: नरक आयु का बंध बहु-आरंभ और बहु-परिग्रह से होता है। "श्वभ्र" नरक का नाम है और "सागर" उसकी विशालता और पार करने की कठिनाई बताता है।'),
 terms=[('संक्लेश', 'distressed, violent state of mind', 'दुःखी और हिंसक मनोभाव'), ('श्वभ्र', 'hell', 'नरक')],
 title=('The road to hell', 'नरक की ओर')))
d1.append(u('9', "तहाँ भूमि परसत दुख इसो, बिच्छू सहस डसै नहिं तिसो।\nतहाँ राध-श्रोणित वाहिनी, कृमि-कुल-कलित, देह-दाहिनी॥",
 ('In hell, the pain of merely touching the ground is greater than the sting of a thousand scorpions. There flow rivers (the Vaitarani) of pus and blood, full of swarms of worms, which burn the body.',
  'वहाँ भूमि को छूने भर से इतना दुःख होता है जितना हज़ार बिच्छू के डंक से भी नहीं होता। वहाँ पीब और रक्त की नदियाँ बहती हैं, जो कीड़ों के समूह से भरी और शरीर को जलाने वाली हैं।'),
 ('The poet gives a comparison for the unimaginable: the ground of hell hurts more than a thousand scorpion stings. Rivers (named Vaitarani in the Agam) of pus (radh) and blood (shronit) swarm with worms (krimi-kul) and burn the body. The jiva in hell has a body called Vaikriyik that does not die even when cut, so the suffering continues for the full life span.',
  'अकल्पनीय को समझाने के लिए कवि तुलना देते हैं: नरक की भूमि का स्पर्श हज़ार बिच्छुओं के डंक से अधिक कष्ट देता है। राध (पीब) और श्रोणित (रक्त) की नदियाँ (आगम में वैतरणी) कीड़ों के झुंड से भरी हैं और शरीर को जलाती हैं। नरक के जीव का वैक्रियिक शरीर कटने पर भी मरता नहीं, इसलिए आयु पूरी होने तक दुःख चलता रहता है।'),
 terms=[('राध', 'pus', 'पीब'), ('श्रोणित', 'blood', 'रक्त'), ('कृमि', 'worms', 'कीड़े')],
 title=('Land and rivers of hell', 'नरक की भूमि और नदियाँ')))
d1.append(u('10', "सेमर तरु दल जुत असिपत्र, असि ज्यों देह विदारैं तत्र।\nमेरु समान लोह गलि जाय, ऐसी शीत उष्णता थाय॥",
 ('There the Semar (silk-cotton) trees have leaves like swords, which tear the body like blades. The heat is such that an iron lump as big as Mount Meru would melt; the cold is just as extreme.',
  'वहाँ सेमर वृक्ष के पत्ते तलवार जैसे होते हैं, जो तलवार की तरह देह को चीर देते हैं। गर्मी इतनी कि मेरु पर्वत जितना लोहे का पिंड भी गल जाए; और ठंड भी उतनी ही अत्यंत।'),
 ('Three more sufferings: the Semar tree with sword-like leaves (Asipatra), extreme heat (ushnata) and extreme cold (sheet). In the Agam the upper hells are hot and the lowest are cold (the fifth has both), each beyond anything on earth. A lump of iron the size of Mount Meru thrown into the heat there would melt before reaching the ground. The detailed description of the hells is in the Tiloyapannatti and in Tattvartha Sutra chapter 3.',
  'तीन और दुःख: तलवार जैसे पत्तों वाला सेमर (असिपत्र) वृक्ष, अत्यंत गर्मी (उष्णता) और अत्यंत सर्दी (शीत)। आगम के अनुसार ऊपर के नरक उष्ण और सबसे नीचे के शीत हैं (पाँचवें में दोनों), पृथ्वी की किसी भी गर्मी-सर्दी से कहीं अधिक। वहाँ की गर्मी में मेरु पर्वत के बराबर लोहे का पिंड डालें तो भूमि तक पहुँचने से पहले गल जाए। नरकों का विस्तृत वर्णन तिलोयपण्णत्ति और तत्त्वार्थ सूत्र अध्याय 3 में है।'),
 terms=[('असिपत्र', 'sword-leaved', 'तलवार जैसे पत्ते'), ('सेमर', 'silk-cotton tree', 'सेमल वृक्ष')],
 title=('Trees, heat and cold', 'वृक्ष, गर्मी और सर्दी')))
d1.append(u('11', "तिल-तिल करैं देह के खण्ड, असुर भिड़ावैं दुष्ट प्रचण्ड।\nसिन्धुनीर तैं प्यास न जाय, तो पण एक न बूँद लहाय॥",
 ('The nark-jivas’ bodies are cut into sesame-seed-sized pieces. Fierce wicked asuras (celestials) make them fight each other. Their thirst could not be quenched even by an ocean of water, yet they do not get a single drop.',
  'नारकी जीवों की देह के तिल-तिल जितने टुकड़े किए जाते हैं। क्रूर और दुष्ट असुर उन्हें आपस में लड़वाते हैं। इनकी प्यास समुद्र का पानी पीने से भी न बुझे, फिर भी इन्हें एक बूँद नहीं मिलती।'),
 ('Four more sufferings: bodies cut up, the cruelty of the Asurkumar devas who incite fights (in the first three hells), and thirst with no water. Like mercury, the Vaikriyik body of the nark rejoins after being cut, so the torture repeats. Nark-jivas also fight each other because of Vibhangavadhi jnana: they can see a past-life enemy.',
  'चार और दुःख: देह का खंड-खंड होना, असुरकुमार देवों की क्रूरता जो (पहले तीन नरकों में) लड़ाई कराते हैं, और प्यास में पानी का अभाव। पारे की तरह नारकी का वैक्रियिक शरीर कटकर फिर जुड़ जाता है, इसलिए यातना दोहराई जाती है। नारकी विभंगावधि ज्ञान से पूर्व-जन्म के वैर को देखकर आपस में भी लड़ते हैं।'),
 terms=[('असुर', 'Asurkumar devas', 'असुरकुमार देव'), ('सिन्धुनीर', 'ocean water', 'समुद्र का जल')],
 title=('Cutting, fighting and thirst', 'खंड-खंड, युद्ध और प्यास')))
d1.append(u('12', "तीनलोक को नाज जु खाय, मिटै न भूख कणा न लहाय।\nये दुख बहु सागर लौं सहै, करम जोग तैं नर गति लहै॥",
 ('Even if one ate all the grain of the three worlds, the hunger would not be satisfied; yet not a single grain is received. These sufferings are borne for many sagaropam years. By some chance of karma the soul at last gets a human birth.',
  'तीनों लोकों का अनाज खा जाए तब भी भूख न मिटे, फिर भी एक दाना नहीं मिलता। ये दुःख बहुत सागरोपम वर्षों तक सहता है। फिर किसी कर्म-योग से मनुष्य गति पाता है।'),
 ('Hunger without food finishes the list of nark sufferings. "Bahu sagar lon" means for many Sagaropam: the maximum life in the 7th hell is 33 Sagaropam (see the Karma Siddhant page for the meaning of Sagaropam). The poet closes the hell section with hope: a human birth follows when the karma is exhausted, through karma-yoga, not by merit of the soul at this stage.',
  'अन्न के बिना भूख, नरक-दुःखों की सूची पूरी करती है। "बहु सागर लौं" यानी अनेक सागरोपम: सातवें नरक में उत्कृष्ट आयु 33 सागरोपम है (सागरोपम का अर्थ कर्म सिद्धांत पृष्ठ पर देखें)। कवि नरक का प्रसंग आशा के साथ समाप्त करते हैं: कर्म क्षीण होने पर मनुष्य जन्म मिलता है, पर यह इस अवस्था में आत्मा के किसी पुरुषार्थ से नहीं, कर्म-योग से।'),
 title=('Hunger, and escape', 'भूख और वहाँ से निकलना')))
d1.append(u('13', "जननी उदर वस्यो नव मास, अंग सकुचतैं पायो त्रास।\nनिकसत जे दुख पाये घोर, तिनको कहत न आवै ओर॥",
 ('In the mother’s womb the soul lived for nine months, with its limbs cramped and suffered distress. The terrible pain at birth is beyond all telling.',
  'माता के पेट में नौ महीने रहा; अंग सिकुड़े हुए थे, इसलिए कष्ट पाया। जन्म के समय जो घोर दुःख हुए, उनका अंत नहीं कहा जा सकता।'),
 ('Human life is the rarest and the best chance, yet it begins in suffering: nine months in a cramped womb, then the pain of birth. The verse tells us not to be proud of the body: its beginning was pain. "Ore" means limit or end: the sufferings have no end that words can reach.',
  'मनुष्य जन्म सबसे दुर्लभ और सर्वोत्तम अवसर है, फिर भी उसकी शुरुआत कष्ट से होती है: नौ महीने तंग गर्भ में और फिर जन्म की पीड़ा। यह पद शरीर पर अभिमान न करने की सीख देता है: उसका आरंभ ही दुःख है। "ओर" यानी सीमा या अंत: दुःखों का ऐसा अंत नहीं जिसे शब्द छू सकें।'),
 title=('Birth and the womb', 'गर्भवास और जन्म')))
d1.append(u('14', "बालपने में ज्ञान न लह्यो, तरुण समय तरुणी-रत रह्यो।\nअर्द्धमृतकसम बूढ़ापनो, कैसे रूप लखै आपनो॥",
 ('In childhood it gained no knowledge. In youth it remained absorbed in women. Old age is like being half dead: then how could it see its own self?',
  'बचपन में ज्ञान नहीं पाया। जवानी में स्त्रियों में लीन रहा। बुढ़ापा अधमरे जैसा है: फिर अपना स्वरूप कैसे देख पाए?'),
 ('The three ages of man pass without self-knowledge: childhood in ignorance, youth in sensual attachment, old age in weakness. The question at the end is the heart of the verse: "kaise roop lakhai apano?", how will one see one’s own nature? The poet is pushing the listener to begin now, in whichever age he is. (The verse speaks from the male perspective of the traditional audience; the lesson applies equally to every human being.)',
  'मनुष्य की तीनों अवस्थाएँ आत्म-ज्ञान के बिना बीत जाती हैं: बचपन अज्ञान में, जवानी विषय-आसक्ति में, बुढ़ापा दुर्बलता में। अंतिम प्रश्न इस पद का सार है: "कैसे रूप लखै आपनो?", अपना स्वरूप कैसे देखे? कवि श्रोता को प्रेरित कर रहे हैं कि जिस अवस्था में हो, अभी आरंभ करो। (पद पारंपरिक पुरुष श्रोता के दृष्टिकोण से है; शिक्षा हर मनुष्य के लिए समान है।)'),
 title=('Childhood, youth, old age', 'बचपन, यौवन, बुढ़ापा')))
d1.append(u('15', "कभी अकामनिर्जरा करै, भवनत्रिक में सुर तन धरै।\nविषय-चाह-दावानल दह्यो, मरत विलाप करत दुख सह्यो॥",
 ('Sometimes through Akama-nirjara (shedding of karma unwillingly, without intent) the soul takes a celestial body among the Bhavan-trik (Bhavanvasi, Vyantar, Jyotishk gods). There it is burnt by the forest-fire of desire for sense pleasures and, at death, lamenting, suffers pain.',
  'कभी अकाम निर्जरा (बिना इच्छा के, परवशता में कर्म झड़ना) के फलस्वरूप भवनत्रिक (भवनवासी, व्यंतर, ज्योतिष्क) में देव का शरीर पाता है। वहाँ विषयों की चाह की दावानल से जलता है और मरते समय विलाप करता हुआ दुःख सहता है।'),
 ('Akama-nirjara happens when a person suffers hunger, thirst or captivity without wanting it and without anger, so some karma is shed (Tattvartha Sutra 6.20 gives it as one cause of celestial birth). The god enjoys pleasures but burns with desire for more, and is full of jealousy of those greater. At the end of life he knows the signs of death (garland fading) and laments. Dev gati is not liberation: it is another turn of the wheel.',
  'अकाम निर्जरा तब होती है जब कोई भूख, प्यास या बंधन का कष्ट इच्छा के बिना और क्रोध किए बिना सहता है, जिससे कुछ कर्म झड़ते हैं (तत्त्वार्थ सूत्र 6.20 इसे देवायु का एक कारण बताता है)। देव सुख भोगता है पर और की चाह में जलता है और बड़े देवों से ईर्ष्या करता है। आयु के अंत में मरण के चिह्न (माला मुरझाना आदि) देखकर वह विलाप करता है। देवगति मोक्ष नहीं, संसार-चक्र का एक और मोड़ है।'),
 terms=[('अकामनिर्जरा', 'involuntary shedding of karma', 'बिना इच्छा के कर्म-निर्जरा'), ('भवनत्रिक', 'Bhavanvasi, Vyantar, Jyotishk gods', 'भवनवासी, व्यंतर, ज्योतिष्क'), ('दावानल', 'forest-fire', 'जंगल की आग')],
 title=('Dev gati: first three orders', 'देवगति: भवनत्रिक')))
d1.append(u('16', "जो विमानवासी हू थाय, सम्यग्दर्शन बिन दुख पाय।\nतहँतैं चय थावर तन धरै, यों परिवर्तन पूरे करै॥",
 ('Even if the soul becomes a Vimanvasi (Vaimanik) god, without right faith (samyagdarshan) it suffers. From there it falls (chaya) and takes a one-sensed Sthavar body, and thus completes the cycles of rebirth.',
  'यदि वैमानिक (विमानवासी) देव भी हो जाए, तो भी सम्यग्दर्शन के बिना दुःख ही पाता है। वहाँ से च्युत होकर स्थावर (एकेन्द्रिय) शरीर धारण करता है, और इस प्रकार परिवर्तन (संसार-चक्र) पूरे करता रहता है।'),
 ('This verse closes the Dhal and gives the main lesson: the highest heaven is not safe. Without samyagdarshan a god can still fall to a one-sensed body. "Parivartan" refers to the five parivartans of the soul’s endless wandering: dravya, kshetra, kal, bhava (births) and bhava (inner feelings). The solution is promised for Dhal 3: samyagdarshan. But first Dhal 2 explains what exactly stands in the way: mithyatva.',
  'यह पद ढाल का समापन करता है और मुख्य शिक्षा देता है: सबसे ऊँचा स्वर्ग भी सुरक्षित नहीं। सम्यग्दर्शन के बिना देव भी एकेन्द्रिय शरीर में गिर सकता है। "परिवर्तन" से आत्मा के अनंत भ्रमण के पाँच परिवर्तन सूचित हैं: द्रव्य, क्षेत्र, काल, भव और भाव। समाधान तीसरी ढाल में बताया जाएगा: सम्यग्दर्शन। पर पहले दूसरी ढाल बताती है कि बाधा क्या है: मिथ्यात्व।'),
 terms=[('विमानवासी', 'Vaimanik gods (Kalpa and beyond)', 'वैमानिक देव'), ('चय', 'falling (death of a god)', 'च्यवन, देव का मरण'), ('परिवर्तन', 'cycle of rebirth', 'संसार-चक्र')],
 title=('Even heaven is not safe', 'स्वर्ग भी सुरक्षित नहीं')))

def sec(id_, nav, title, intro, units, diagram=''):
    return dict(id=id_, nav=nav, title=title, intro=intro, units=units, diagram=diagram)

d1_intro = ('<div class="card">' + bd(
  'Dhal 1 answers a single question: <b>why is the soul unhappy?</b> The poet walks through the four gatis (nigod and animals, hell, humans, gods) and shows that suffering is found in all of them, so no gati by itself is a refuge. The root cause, named at once, is moha. Use the wheel to see the whole route, then read the verses in order.',
  'पहली ढाल एक ही प्रश्न का उत्तर देती है: <b>आत्मा दुःखी क्यों है?</b> कवि चारों गतियों (निगोद-पशु, नरक, मनुष्य, देव) में घूमकर दिखाते हैं कि दुःख सभी में है, इसलिए कोई गति अपने आप में शरण नहीं। मूल कारण, मोह, तुरंत बता दिया गया है। पूरा मार्ग समझने के लिए चक्र देखें, फिर पद क्रम से पढ़ें।') + '</div>')

DHAL1 = dict(
    path='chhah-dhala/dhal-1.html', title=('Chhahdhala · First Dhal', 'छहढाला · पहली ढाल'),
    by=('Pt. Daulatram · Sansar-dukh (suffering of the cycle of birth and death)', 'पं. दौलतराम · संसार के दुःख'),
    desc='Chhahdhala first dhal: original verses, Hindi and English meaning and illustrated explanation.',
    crumbs=[('chhah-dhala/', ('Chhah Dhala', 'छहढाला'))],
    next=('dhal-2.html', ('Second Dhal', 'दूसरी ढाल')), prev=('./', ('Chhah Dhala', 'छहढाला')),
    intro=d1_intro, foot=FOOT_OK,
    sections=[
      sec('map', ('The cycle', 'चक्र'), ('The cycle of the four gatis', 'चारों गतियों का चक्र'),
          ('Where the soul has been and where the verses take us.', 'आत्मा कहाँ-कहाँ रही और पद हमें कहाँ ले जाते हैं।'), [], wheel() + DUKH_TABLE),
      sec('s1', ('Aim', 'प्रयोजन'), ('Mangalacharan and the aim', 'मंगलाचरण और प्रयोजन'), None, d1[0:3]),
      sec('s2', ('Nigod', 'निगोद'), ('Nigod and one-sensed beings', 'निगोद और एकेन्द्रिय'), None, d1[3:5]),
      sec('s3', ('Animals', 'तिर्यंच'), ('Tras and Tiryanch gati', 'त्रस और तिर्यंच गति'), None, d1[5:8]),
      sec('s4', ('Hell', 'नरक'), ('Narak gati', 'नरक गति'), None, d1[8:12],
          flow([fbox('Heavy violence and sanklesh', 'अति हिंसा और संक्लेश', 'red'), arrow('rd'),
                fbox('Narak-ayu bound', 'नरक-आयु का बंध', 'gold'), arrow('rd'),
                fbox('Birth in hell: cold, heat, hunger, thirst, fights', 'नरक में जन्म: शीत, उष्ण, भूख, प्यास, युद्ध', 'red'), arrow('rd'),
                fbox('Ayu exhausted: human birth by karma-yoga', 'आयु पूर्ण: कर्मयोग से मनुष्य जन्म', 'green')])),
      sec('s5', ('Human', 'मनुष्य'), ('Manushya gati', 'मनुष्य गति'), None, d1[12:14],
          flow([fbox('Womb', 'गर्भवास', 'acc', ('9 months', '9 मास')), arrow('rd'), fbox('Childhood', 'बाल्य', 'acc', ('ignorance', 'अज्ञान')), arrow('rd'),
                fbox('Youth', 'यौवन', 'acc', ('sense pleasures', 'विषयासक्ति')), arrow('rd'), fbox('Old age', 'वृद्ध', 'acc', ('weakness', 'दुर्बलता'))])),
      sec('s6', ('Gods', 'देव'), ('Dev gati', 'देव गति'), None, d1[14:17],
          flow([fbox('Akama-nirjara', 'अकाम निर्जरा', 'gold'), arrow('rd'), fbox('Bhavan-trik god', 'भवनत्रिक देव', 'teal'), arrow('rd'),
                fbox('Desire, jealousy, lament at death', 'चाह, ईर्ष्या, मरण का विलाप', 'red'), arrow('rd'),
                fbox('Fall to Sthavar (even from Vimanvasi without samyagdarshan)', 'स्थावर में पतन (विमानवासी भी सम्यग्दर्शन बिना)', 'red')])),
    ])

# ======================= DHAL 2 =======================
d2 = []
d2.append(u('1', "ऐसे मिथ्यादृग-ज्ञान-चरन, वश भ्रमत भरत दुःख जन्म-मरन।\nतातैं इनको तजिये सुजान, सुन तिन संक्षेप कहूँ बखान॥",
 ('Under the influence of such wrong faith (mithyadarshan), wrong knowledge (mithyajnan) and wrong conduct (mithyacharitra), the soul wanders and suffers birth and death. Therefore, wise one, give them up. Listen, I will describe them briefly.',
  'ऐसे मिथ्यादर्शन, मिथ्याज्ञान और मिथ्याचारित्र के वश होकर जीव भटकता है और जन्म-मरण के दुःख भरता है। इसलिए हे सुज्ञ, इन्हें छोड़ो। सुनो, मैं इन्हें संक्षेप में बताता हूँ।'),
 ('Dhal 1 ended with the question "why does the soul wander?". This verse answers: because of mithyatva in its three forms: wrong faith, wrong knowledge, wrong conduct. They are the opposite of the Ratnatraya of Tattvartha Sutra 1.1. The poet will first describe each as Agrihit (natural, from beginningless time) and then Grihit (taken up in this life from false teachers).',
  'पहली ढाल का प्रश्न था: "जीव क्यों भटकता है?" यह पद उत्तर देता है: मिथ्यात्व के तीन रूपों के कारण: मिथ्यादर्शन, मिथ्याज्ञान, मिथ्याचारित्र। ये तत्त्वार्थ सूत्र 1.1 के रत्नत्रय के विपरीत हैं। कवि पहले प्रत्येक को अगृहीत (स्वाभाविक, अनादि से) और फिर गृहीत (इसी जन्म में कुगुरु आदि से ग्रहण किया) रूप में बताएँगे।'),
 terms=[('मिथ्यादृग', 'wrong faith', 'मिथ्यादर्शन'), ('चरन', 'conduct', 'चारित्र'), ('सुजान', 'wise person', 'ज्ञानी जन')],
 title=('The three wrongs', 'तीन मिथ्यात्व')))
d2.append(u('2', "जीवादि प्रयोजनभूत तत्त्व, सरधैं तिनमाँहिं विपर्ययत्व।\nचेतन को है उपयोग रूप, विनमूरत चिन्मूरत अनूप॥",
 ('Belief about the Jiva and the other purposeful tattvas is perverse (viparyaya). The soul has upayoga (consciousness) as its form; it is without a body (amurtik), a form of knowing (chinmurti) and incomparable.',
  'जीव आदि प्रयोजनभूत तत्त्वों की श्रद्धा में विपरीतता है। (सही स्वरूप यह है:) चेतन का स्वरूप उपयोग है; वह अमूर्तिक (बिना आकार का), चिन्मूर्ति (चैतन्य-मय) और अनुपम है।'),
 ('Agrihit mithyadarshan starts here: wrong belief about the seven tattvas, which the soul holds even without anyone teaching it. The poet first gives the correct nature of the soul: upayoga (jnana and darshan), formless, a knower. Note the difference: Jiva is not matter (pudgal), though it lives with a body. Tattvartha Sutra 1.4 lists the seven tattvas.',
  'अगृहीत मिथ्यादर्शन यहाँ से आरंभ होता है: सात तत्त्वों के विषय में विपरीत श्रद्धा, जो किसी के सिखाए बिना भी जीव में अनादि से है। कवि पहले आत्मा का सही स्वरूप बताते हैं: उपयोग (ज्ञान-दर्शन) रूप, अमूर्तिक, ज्ञायक। ध्यान दें: जीव पुद्गल नहीं है, यद्यपि शरीर के साथ रहता है। सात तत्त्व तत्त्वार्थ सूत्र 1.4 में गिनाए हैं।'),
 terms=[('उपयोग', 'upayoga: consciousness (jnana and darshan)', 'ज्ञान-दर्शन रूप चेतना'), ('चिन्मूरत', 'form of consciousness', 'चैतन्य-स्वरूप'), ('अनूप', 'incomparable', 'अनुपम')],
 title=('The soul as it is', 'आत्मा का सही स्वरूप')))
d2.append(u('3', "पुद्गल नभ धर्म अधर्म काल, इनतैं न्यारी है जीव चाल।\nताकों न जान विपरीत मान, करि करै देह में निज पिछान॥",
 ('The Jiva is different in nature from pudgal (matter), akash (space), dharma, adharma and kal (time). But the soul does not know it so; holding the opposite belief, it takes the body to be itself.',
  'पुद्गल, आकाश, धर्म, अधर्म और काल इन सबसे जीव की चाल (स्वभाव) भिन्न है। परंतु जीव इसे नहीं जानता और उलटी मान्यता करके देह में ही अपनापन मानता है।'),
 ('The five ajiva dravyas are named: pudgal, akash, dharma, adharma, kal; with Jiva they make the six dravyas. The mistake in Jiva-tattva is called Dehatma-buddhi (taking the body as the self). It is the root of all the other wrong beliefs that follow in the next verses.',
  'पाँच अजीव द्रव्य गिनाए हैं: पुद्गल, आकाश, धर्म, अधर्म, काल; जीव को मिलाकर छह द्रव्य। जीव तत्त्व की भूल को देहात्म-बुद्धि (देह को ही आत्मा मानना) कहते हैं। यही आगे के सभी मिथ्या विश्वासों की जड़ है।'),
 terms=[('पुद्गल', 'matter', 'जड़ पदार्थ'), ('नभ', 'akash: space', 'आकाश'), ('न्यारी', 'distinct', 'भिन्न')],
 title=('Jiva-tattva: body as self', 'जीव तत्त्व: देह में अपनापन')))
d2.append(u('4', "मैं सुखी दुखी मैं रंक राव, मेरे धन गृह गोधन प्रभाव।\nमेरे सुत तिय मैं सबल दीन, बेरूप सुभग मूरख प्रवीन॥",
 ('"I am happy, I am unhappy, I am a pauper, I am a king; my wealth, house, cattle and influence; my son, my wife; I am strong, I am weak, ugly, handsome, foolish, clever": all this is thought by the one who mistakes the body for himself.',
  '"मैं सुखी हूँ, दुखी हूँ, गरीब हूँ, राजा हूँ; मेरे धन, घर, पशु और प्रभाव; मेरे पुत्र, मेरी स्त्री; मैं बलवान हूँ, दुर्बल हूँ, कुरूप हूँ, सुंदर हूँ, मूर्ख हूँ, चतुर हूँ": ऐसा विचार वही करता है जो शरीर को अपना मान बैठा है।'),
 ('This verse lists the many "I am" and "my" claims. Each belongs to the body or to outside things, none to the soul. The verse teaches the practice of Bhed-vijnan: separating "I" (the knower) from "mine" (wealth, family, body qualities). It is also a mirror: read it line by line and notice which of these we say about ourselves every day.',
  'यह पद "मैं" और "मेरे" के अनेक दावों की सूची है। ये सब शरीर या बाहरी वस्तुओं के हैं, आत्मा के नहीं। यह भेद-विज्ञान का अभ्यास सिखाता है: "मैं" (ज्ञाता) को "मेरे" (धन, परिवार, शरीर के गुण) से अलग करना। यह दर्पण भी है: एक-एक पंक्ति पढ़कर देखें कि इनमें से कौन-सी बातें हम रोज़ अपने बारे में कहते हैं।'),
 terms=[('रंक', 'poor man', 'निर्धन'), ('राव', 'king, rich', 'राजा'), ('गोधन', 'cattle wealth', 'गाय-बैल आदि पशुधन'), ('तिय', 'wife', 'स्त्री')],
 title=('"I" and "mine"', '"मैं" और "मेरे"')))
d2.append(u('5', "तन उपजत अपनी उपज जान, तन नशत आपको नाश मान।\nरागादि प्रगट ये दुःख देन, तिनही को सेवत गिनत चैन॥",
 ('When the body is born, he thinks "I am born"; when the body dies, he thinks "I am destroyed" (this is the wrong belief about Ajiva-tattva). Attachment and the like (ragadi) clearly give pain, yet he serves them and thinks it is comfort (the wrong belief about Asrav-tattva).',
  'शरीर उत्पन्न होता है तो अपनी उत्पत्ति मानता है; शरीर नष्ट होता है तो अपना नाश मानता है (यह अजीव तत्त्व की भूल है)। राग आदि भाव स्पष्ट रूप से दुःख देने वाले हैं, फिर भी उन्हीं का सेवन करता है और उसे चैन मानता है (यह आस्रव तत्त्व की भूल है)।'),
 ('Two tattvas in one verse. Ajiva-tattva: the body (pudgal) is born and dies, but the soul is neither born nor destroyed; thinking otherwise is a wrong belief. Asrav-tattva: ragadi (attachment, aversion) are the cause of the inflow of karma and give pain (akulata); to enjoy them and feel they are pleasant is the wrong belief.',
  'एक पद में दो तत्त्व। अजीव तत्त्व: शरीर (पुद्गल) उत्पन्न होता और नष्ट होता है, पर आत्मा न उत्पन्न होती है, न नष्ट; ऐसा न मानना भूल है। आस्रव तत्त्व: राग-द्वेष कर्मों के आगमन के कारण हैं और आकुलता (दुःख) देते हैं; उन्हें सुखद मानकर भोगना भूल है।'),
 terms=[('रागादि', 'attachment, aversion and other impure feelings', 'राग-द्वेष आदि विकारी भाव')],
 title=('Ajiva and Asrav', 'अजीव और आस्रव')))
d2.append(u('6', "शुभ-अशुभ बंध के फल मँझार, रति-अरति करै निज पद विसार।\nआतम हित हेतु विराग ज्ञान, ते लखै आपको कष्टदान॥",
 ('In the fruits of shubh and ashubh bandh (good and bad karma bondage) he feels liking (rati) and dislike (arati), forgetting his own state. Detachment (vairagya) and knowledge, which are the cause of the soul’s welfare, he sees as giving pain to himself.',
  'शुभ और अशुभ कर्मबंध के फल में वह रति और अरति करता है और अपना निज पद भूल जाता है। आत्महित के कारण वैराग्य और ज्ञान को वह अपने लिए कष्टदायक देखता है।'),
 ('Bandh-tattva wrong belief: he thinks good karma (punya) is the goal and enjoys its fruit; he dislikes the fruit of papa. In fact both are bondage (see Tattvartha Sutra 8.25–26: punya and papa both belong to the bandh of karma). The sad part of the verse is the second half: vairagya and jnana, the true helpers, look like burdens to the one under mithyatva.',
  'बंध तत्त्व की भूल: वह पुण्य को लक्ष्य मानकर उसके फल में रति करता है और पाप के फल में अरति। वस्तुतः दोनों बंध हैं (तत्त्वार्थ सूत्र 8.25–26: पुण्य और पाप दोनों कर्म-बंध के ही भेद हैं)। पद का करुण भाग दूसरी पंक्ति है: वैराग्य और ज्ञान, जो सच्चे सहायक हैं, मिथ्यादृष्टि को बोझ लगते हैं।'),
 terms=[('रति', 'liking', 'राग'), ('अरति', 'dislike', 'द्वेष'), ('विराग', 'detachment', 'वैराग्य')],
 title=('Bandh-tattva', 'बंध तत्त्व')))
d2.append(u('7', "रोकी न चाह निजशक्ति खोय, शिवरूप निराकुलता न जोय।\nयाही प्रतीतिजुत कछुक ज्ञान, सो दुखदायक अज्ञान जान॥",
 ('He does not stop his desire (chah), which wastes his own strength (this is the wrong belief about Samvar and Nirjara). He does not see the peace without anxiety (nirakulata) which is the form of liberation (the wrong belief about Moksha). The knowledge he has along with this wrong belief is painful ignorance (agrihit mithyajnana).',
  'वह चाह को रोकता नहीं, जिससे अपनी शक्ति खोता है (संवर और निर्जरा की भूल)। मोक्ष का स्वरूप जो निराकुलता है, उसे नहीं देखता (मोक्ष तत्त्व की भूल)। इसी विपरीत श्रद्धा के साथ जो थोड़ा-बहुत ज्ञान है, वह दुःख देने वाला अज्ञान (अगृहीत मिथ्याज्ञान) जानो।'),
 ('This verse finishes the seven tattvas: Samvar and Nirjara (stopping desire and shedding karma) and Moksha (nirakul, anxiety-free bliss). It also defines Agrihit Mithyajnana: even knowledge becomes ignorance if it goes with a false faith, just as good milk turns sour in a bad vessel. (This matches Tattvartha Sutra 1.31–32: matijnan, shrutajnan and avadhijnan become wrong knowledge when held by one without right faith.)',
  'यह पद सात तत्त्वों की भूलें पूरी करता है: संवर-निर्जरा (चाह रोकना और कर्म झड़ाना) और मोक्ष (निराकुल आनंद)। साथ ही अगृहीत मिथ्याज्ञान का लक्षण भी देता है: मिथ्या श्रद्धा के साथ ज्ञान भी अज्ञान हो जाता है, जैसे अच्छा दूध खराब बर्तन में फट जाता है। (यह तत्त्वार्थ सूत्र 1.31–32 से मेल खाता है: मिथ्यादृष्टि का मति, श्रुत और अवधि ज्ञान विपरीत हो जाता है।)'),
 terms=[('निराकुलता', 'freedom from anxiety', 'आकुलता का अभाव'), ('प्रतीति', 'belief', 'श्रद्धा')],
 title=('Samvar, Nirjara, Moksha; Agrihit mithyajnan', 'संवर, निर्जरा, मोक्ष; अगृहीत मिथ्याज्ञान')))
d2.append(u('8', "इन जुत विषयनि में जो प्रवृत्त, ताको जानो मिथ्याचरित्त।\nयों मिथ्यात्वादि निसर्ग जेह, अब जे गृहीत, सुनिये सु तेह॥",
 ('Engaging in the objects of the senses together with these (wrong belief and wrong knowledge) is wrong conduct (mithyacharitra). These are the natural (nisarga, agrihit) forms of mithyatva. Now hear about the acquired (grihit) ones.',
  'इन (मिथ्या श्रद्धा और ज्ञान) के साथ विषयों में प्रवृत्ति करना मिथ्याचारित्र जानो। ये मिथ्यात्व आदि स्वाभाविक (निसर्गज, अगृहीत) हैं। अब जो गृहीत (ग्रहण किए हुए) हैं, उन्हें सुनो।'),
 ('Agrihit mithyacharitra is the third wrong. Agrihit means "not taken up": it exists from beginningless time without anyone’s teaching, as in animals and children. This also explains the whole structure of the Dhal: first the three agrihit (verses 2–8), then the three grihit (verses 9–14).',
  'अगृहीत मिथ्याचारित्र तीसरी भूल है। अगृहीत का अर्थ है "बिना ग्रहण किए": यह अनादि से बिना किसी के सिखाए है, जैसा पशुओं और बच्चों में दिखता है। इससे पूरी ढाल की रचना भी स्पष्ट होती है: पहले तीनों अगृहीत (पद 2–8), फिर तीनों गृहीत (पद 9–14)।'),
 terms=[('निसर्ग', 'natural, innate', 'स्वभाव से, सहज'), ('गृहीत', 'acquired', 'ग्रहण किया हुआ')],
 title=('Agrihit mithyacharitra', 'अगृहीत मिथ्याचारित्र')))
d2.append(u('9', "जो कुगुरु कुदेव कुधर्म सेव, पोखैं चिर दर्शनमोह एव।\nअन्तर रागादिक धरैं जेह, बाहर धन अम्बरतैं सनेह॥",
 ('Those who serve false Gurus, false Gods and false Dharma nourish the delusion of wrong faith (darshan-moha) for a long time. (The false Guru is one who) holds attachment and the like inside, and outside loves wealth and clothes.',
  'जो कुगुरु, कुदेव और कुधर्म की सेवा करते हैं, वे दर्शनमोह (मिथ्या श्रद्धा) को चिरकाल तक पोषण देते हैं। (कुगुरु वे हैं) जो भीतर राग आदि धारण करते हैं और बाहर धन तथा वस्त्र से स्नेह रखते हैं।'),
 ('Grihit mithyadarshan has three objects: Kugur, Kudev, Kudharma. This verse names them and starts with the first, the false Guru, who has attachment inside and love for wealth (dhan) and clothes (ambar) outside. In the Digambar view the true Guru is Nirgranth (without any possession) and Digambar (sky-clad); a person who keeps wealth or clothes cannot be a Nirgranth Guru, even though he may be well-respected.',
  'गृहीत मिथ्यादर्शन के तीन विषय हैं: कुगुरु, कुदेव, कुधर्म। यह पद तीनों का नाम लेकर पहले कुगुरु का लक्षण देता है: भीतर राग, और बाहर धन तथा वस्त्र से स्नेह। दिगंबर परंपरा में सच्चे गुरु निर्ग्रंथ (परिग्रह-रहित) और दिगंबर होते हैं; जो धन या वस्त्र रखे वह निर्ग्रंथ गुरु नहीं हो सकता, भले ही वह सम्माननीय हो।'),
 terms=[('कुगुरु', 'false guru', 'झूठा गुरु'), ('कुदेव', 'false deity', 'झूठा देव'), ('दर्शनमोह', 'darshan-moha: delusion of faith', 'श्रद्धा का मोह'), ('अम्बर', 'clothing', 'वस्त्र')],
 title=('Grihit mithyadarshan', 'गृहीत मिथ्यादर्शन')))
d2.append(u('10', "धारैं कुलिंग लहि महत भाव, ते कुगुरु जन्मजल उपलनाव।\nजो राग-द्वेष मलकरि मलीन, वनिता गदादिजुत चिह्न चीन॥",
 ('Those who wear a false garb and take pride in their greatness are false Gurus: like a stone boat they sink in the ocean of birth. (A false God is) one who is stained with the filth of attachment and aversion, and is recognised by signs like a woman or a mace (in hand).',
  'जो कुलिंग (झूठा वेष) धारण करके अपने को महान मानते हैं वे कुगुरु हैं; वे पत्थर की नाव की तरह संसार-सागर में डूबते हैं। (कुदेव वे हैं) जो राग-द्वेष रूपी मैल से मलिन हैं और स्त्री, गदा आदि चिह्नों से पहचाने जाते हैं।'),
 ('Two images: the false Guru is a stone boat (upal-nav): it looks like a boat but sinks with those who board it. The false God is recognised by attachment-signs: a woman beside him, weapons like the mace. A true deity has no such signs because he has no raga-dvesha: he is Vitaraga. The test is simple, in the Digambar view: does he have attachment and aversion?',
  'दो उपमाएँ: कुगुरु पत्थर की नाव (उपलनाव) है: दिखने में नाव, पर चढ़ने वालों को लेकर डूबती है। कुदेव राग के चिह्नों से पहचाना जाता है: साथ में स्त्री, हाथ में गदा-शस्त्र। सच्चे देव में ऐसे चिह्न नहीं होते, क्योंकि वे राग-द्वेष रहित, वीतराग हैं। दिगंबर दृष्टि में कसौटी सरल है: क्या उनमें राग-द्वेष है?'),
 terms=[('कुलिंग', 'false outer garb', 'झूठा वेष'), ('उपलनाव', 'stone boat', 'पत्थर की नाव'), ('गदा', 'mace', 'गदा')],
 title=('Kuguru and Kudev', 'कुगुरु और कुदेव')))
d2.append(u('11', "ते हैं कुदेव तिनकी जु सेव, शठ करत न तिन भवभ्रमण छेव।\nरागादि भावहिंसा समेत, दर्वित त्रस थावर मरण खेत॥",
 ('Such are the false Gods; the fool who serves them does not see the end of his wanderings in births. (False Dharma is that) which includes bhav-himsa (violence of passions) and dravya-himsa, the killing of mobile and immobile beings.',
  'वे कुदेव हैं; उनकी सेवा करने वाला मूर्ख अपने भव-भ्रमण का अंत नहीं पाता। (कुधर्म वह है) जिसमें रागादि भाव-हिंसा और त्रस-स्थावर जीवों का घात (द्रव्य-हिंसा) हो।'),
 ('Here Kudharma begins: where there is himsa, either of feelings (bhav-himsa, anger, desire) or of living things (dravya-himsa), there is no dharma. This follows the Digambar view that Ahimsa is the heart of Jain dharma (Tattvartha Sutra chapter 7). "Shath" means fool: not a hard word but a plain statement that serving a false God cannot end the cycle.',
  'यहाँ कुधर्म शुरू होता है: जहाँ हिंसा है, भाव-हिंसा (क्रोध, चाह) या द्रव्य-हिंसा (जीवघात), वहाँ धर्म नहीं। यह दिगंबर मान्यता के अनुरूप है कि अहिंसा जैन धर्म का हृदय है (तत्त्वार्थ सूत्र अध्याय 7)। "शठ" यानी मूर्ख: यह कठोर शब्द नहीं, सीधा कथन है कि कुदेव की सेवा से संसार-चक्र नहीं रुक सकता।'),
 terms=[('भावहिंसा', 'violence in thought and feeling', 'भाव में हिंसा'), ('दर्वित', 'dravya: physical', 'द्रव्य रूप')],
 title=('Kudharma', 'कुधर्म')))
d2.append(u('12', "जे क्रिया तिन्हैं जानत सुधर्म, तिन सरधैं जीव लहै अशर्म।\nयाकूँ गृहीत मिथ्यात्व जान, अब सुन गृहीत जो है अज्ञान॥",
 ('Those who regard such acts as true dharma and believe in them, attain misery (ashrama). Know this as grihit mithyatva. Now hear about the grihit ignorance (mithyajnana).',
  'जो ऐसी क्रियाओं को सच्चा धर्म मानते और उनमें श्रद्धा करते हैं, वे दुःख (अशर्म) पाते हैं। इसे गृहीत मिथ्यात्व जानो। अब गृहीत अज्ञान (मिथ्याज्ञान) सुनो।'),
 ('This verse summarises grihit mithyadarshan (kugur, kudev, kudharma and their worship) and links to the next topic. "Ashrama" is the opposite of "sharma", which means happiness. Thus the poet repeats his main teaching: false faith brings pain, true faith brings the happiness the soul wants (Dhal 1 verse 1).',
  'यह पद गृहीत मिथ्यादर्शन (कुगुरु, कुदेव, कुधर्म और उनकी सेवा) का सार कहता है और अगले विषय को जोड़ता है। "अशर्म" "शर्म" (सुख) का विपरीत है। इस प्रकार कवि अपनी मुख्य शिक्षा दोहराते हैं: मिथ्या श्रद्धा से दुःख मिलता है, सच्ची श्रद्धा से वह सुख जो आत्मा चाहती है (पहली ढाल, पद 1)।'),
 terms=[('अशर्म', 'misery (opposite of sharma, happiness)', 'दुःख'), ('गृहीत', 'taken up from others', 'दूसरों से ग्रहण किया')],
 title=('Summary of grihit mithyatva', 'गृहीत मिथ्यात्व का सार')))
d2.append(u('13', "एकान्तवाद-दूषित समस्त, विषयादिक पोषक अप्रशस्त।\nरागीकुमतनिकृत श्रुताभ्यास, सो है कुबोध बहु देन त्रास॥",
 ('Scriptures that are faulty with ekantavad (one-sided view), that support sense pleasures and are unworthy, composed by passionate (ragi) people of false views: studying them is kubodh (false knowledge), which gives much pain.',
  'जो शास्त्र एकांतवाद से दूषित हैं, विषय-भोग के पोषक और अप्रशस्त हैं, तथा रागी कुमतियों द्वारा रचे गए हैं, उनका अध्ययन कुबोध (मिथ्याज्ञान) है, जो बहुत दुःख देने वाला है।'),
 ('Grihit mithyajnana is defined by three marks of a bad scripture: it is ekant (says "only this" and ignores the other views, against Anekantavad), it supports sensuality, and it was written by a ragi (not a Vitaraga). The Jain test of a true shastra is that it was spoken by the Sarvajna and compiled by the Ganadharas and Acharyas (Dev-Shastra-Guru, see the next Dhal for the true forms).',
  'गृहीत मिथ्याज्ञान की तीन पहचान बताई हैं: एकांत (केवल एक पक्ष मानना, अनेकांत के विरुद्ध), विषय-भोग का पोषण, और रागी (वीतराग नहीं) द्वारा रचित। जैन कसौटी यह है कि सच्चा शास्त्र सर्वज्ञ का कहा और गणधर-आचार्यों द्वारा संकलित हो (सच्चे देव-शास्त्र-गुरु का स्वरूप अगली ढाल में है)।'),
 terms=[('एकान्तवाद', 'one-sided view', 'एकपक्षीय मान्यता'), ('कुबोध', 'false knowledge', 'मिथ्याज्ञान'), ('श्रुताभ्यास', 'study of scripture', 'शास्त्र-अध्ययन')],
 title=('Grihit mithyajnana', 'गृहीत मिथ्याज्ञान')))
d2.append(u('14', "जो ख्याति लाभ पूजादि चाह, धरि करन विविध विध देह दाह।\nआतम अनात्म के ज्ञानहीन, जे जे करनी तन करन छीन॥",
 ('(Grihit mithyacharitra:) Out of desire for fame (khyati), gain (labh), honour (puja) and the like, one undertakes many kinds of tortures of the body. Without knowing the difference between self and non-self, whatever acts he does only weaken the body.',
  '(गृहीत मिथ्याचारित्र:) ख्याति, लाभ, पूजा आदि की चाह से अनेक प्रकार से शरीर को कष्ट देने वाले आचरण करता है। आत्मा और अनात्मा के ज्ञान के बिना वह जो-जो क्रियाएँ करता है, वे केवल देह को क्षीण करती हैं।'),
 ('Austerity (tap) done for fame, gain or honour, and without Atma-Anatma-viveka (knowing the soul from non-soul) is mithya charitra. Observe: the issue is not the fasting or the hardship but the aim and the knowledge behind it. The same fast done with samyagdarshan sheds karma (Tattvartha Sutra 9.3, tapas nirjara cha), but without it only the body weakens.',
  'ख्याति, लाभ या पूजा की चाह से, और आत्मा-अनात्मा के विवेक के बिना किया गया तप मिथ्याचारित्र है। ध्यान दें: दोष उपवास या कष्ट में नहीं, उसके पीछे के उद्देश्य और ज्ञान में है। वही उपवास सम्यग्दर्शन सहित हो तो कर्म-निर्जरा करता है (तत्त्वार्थ सूत्र 9.3, तपसा निर्जरा च), पर उसके बिना केवल शरीर क्षीण होता है।'),
 terms=[('ख्याति', 'fame', 'यश'), ('पूजा', 'honour', 'सम्मान'), ('अनात्म', 'non-self', 'आत्मा से भिन्न')],
 title=('Grihit mithyacharitra', 'गृहीत मिथ्याचारित्र')))
d2.append(u('15', "ते सब मिथ्याचारित्र त्याग, अब आतम के हित पंथ लाग।\nजगजालभ्रमण को देहु त्याग, अब दौलत! निज आतम सुपाग॥",
 ('Give up all this wrong conduct. Now follow the path that is good for the soul. Give up the wandering in the web of the world. Now, Daulat, be absorbed well in your own soul.',
  'यह सब मिथ्याचारित्र छोड़ो। अब आत्मा के हित के मार्ग में लगो। जग-जाल में भ्रमण का त्याग करो। अब, हे दौलत, अपनी आत्मा में भली-भाँति लीन हो जाओ।'),
 ('The Dhal ends with a call to action. Notice the poet addresses himself by his own name, "Daulat": the advice is first for himself and so is humble, not preachy. After showing the problem (three mithyatvas, grihit and agrihit), Dhal 3 will show the cure: Samyagdarshan, Samyagjnan, Samyakcharitra, the Ratnatraya, which is the path to liberation.',
  'ढाल का अंत कर्म के आह्वान से होता है। ध्यान दें कि कवि अपने ही नाम "दौलत" को संबोधित करते हैं: यह उपदेश पहले स्वयं के लिए है, इसलिए विनम्र है, उपदेश-भाव से मुक्त। समस्या (अगृहीत-गृहीत तीनों मिथ्यात्व) दिखाने के बाद तीसरी ढाल में उपाय बताया जाएगा: सम्यग्दर्शन, सम्यग्ज्ञान, सम्यक्चारित्र, यानी रत्नत्रय, जो मोक्ष का मार्ग है।'),
 terms=[('सुपाग', 'well absorbed, steeped in', 'भली-भाँति लीन')],
 title=('Call to the path', 'मार्ग का आह्वान')))

# diagrams for dhal 2
TREE = ('<div class="grid3">' +
        panel(b('1. Mithyadarshan', '१. मिथ्यादर्शन'), '<div class="en"><b>Agrihit</b> (innate): wrong belief in the 7 tattvas, v.2–7<br><b>Grihit</b> (acquired): false Dev, Guru, Dharma, v.9–12</div><div class="hi"><b>अगृहीत</b> (सहज): सात तत्त्वों में विपरीत श्रद्धा, पद 2–7<br><b>गृहीत</b> (ग्रहण किया): कुदेव, कुगुरु, कुधर्म, पद 9–12</div>', 'red') +
        panel(b('2. Mithyajnan', '२. मिथ्याज्ञान'), '<div class="en"><b>Agrihit</b>: knowledge joined with wrong faith, v.7<br><b>Grihit</b>: study of one-sided, passion-written scriptures, v.13</div><div class="hi"><b>अगृहीत</b>: मिथ्या श्रद्धा के साथ ज्ञान, पद 7<br><b>गृहीत</b>: एकांत, रागी-रचित शास्त्रों का अध्ययन, पद 13</div>', 'gold') +
        panel(b('3. Mithyacharitra', '३. मिथ्याचारित्र'), '<div class="en"><b>Agrihit</b>: indulgence in sense objects, v.8<br><b>Grihit</b>: austerity for fame and gain without self-knowledge, v.14</div><div class="hi"><b>अगृहीत</b>: विषयों में प्रवृत्ति, पद 8<br><b>गृहीत</b>: आत्म-ज्ञान बिना ख्याति-लाभ हेतु तप, पद 14</div>', 'teal') +
        '</div>')

TATTVA_TABLE = table(
    [b('Tattva', 'तत्त्व'), b('Wrong belief (mithyatva)', 'विपरीत श्रद्धा'), b('Right belief', 'सही श्रद्धा'), b('Verse', 'पद')],
    [[b('Jiva', 'जीव'), b('Body is "I"; I am rich, poor, strong, weak', 'देह ही "मैं"; मैं धनी, निर्धन, बली, दुर्बल'), b('Soul is a formless knower, distinct from body and all else', 'आत्मा अमूर्तिक ज्ञायक है, शरीर आदि से भिन्न'), '3–4'],
     [b('Ajiva', 'अजीव'), b('Body born = I am born; body dies = I die', 'शरीर का जन्म = मेरा जन्म; शरीर का मरण = मेरा मरण'), b('Body is pudgal; soul is never born or destroyed', 'शरीर पुद्गल है; आत्मा न जन्मती, न मरती'), '5'],
     [b('Asrav', 'आस्रव'), b('Raga-dvesha give comfort', 'राग-द्वेष सुखकारी हैं'), b('Raga-dvesha cause the inflow of karma and give pain', 'राग-द्वेष कर्मों का आस्रव कराते और दुःख देते हैं'), '5'],
     [b('Bandh', 'बंध'), b('Likes fruit of punya, dislikes fruit of papa; vairagya looks painful', 'पुण्य-फल में रति, पाप-फल में अरति; वैराग्य कष्टदायक'), b('Both punya and papa are bondage; detachment and knowledge help the soul', 'पुण्य-पाप दोनों बंध हैं; वैराग्य-ज्ञान आत्मा के हितकारी'), '6'],
     [b('Samvar, Nirjara', 'संवर, निर्जरा'), b('Does not stop desire; wastes his own strength', 'चाह नहीं रोकता; अपनी शक्ति खोता है'), b('Stopping desire stops inflow; austerity with right faith sheds karma', 'चाह रोकने से आस्रव रुकता है; सम्यक् तप से कर्म झड़ते हैं'), '7'],
     [b('Moksha', 'मोक्ष'), b('Does not see anxiety-free bliss', 'निराकुल आनंद को नहीं देखता'), b('Moksha is the state of complete peace of the soul', 'मोक्ष आत्मा की पूर्ण शांति की अवस्था है'), '7']])

TRUE_FALSE = table(
    [b('', ''), b('False', 'झूठा'), b('True (Digambar view)', 'सच्चा (दिगंबर मान्यता)')],
    [[b('Dev', 'देव'), b('Has raga-dvesha; signs such as woman, weapons', 'राग-द्वेष सहित; स्त्री, शस्त्र आदि चिह्न'), b('Vitaraga (no attachment), Sarvajna (all-knowing), Hitopadeshi (teacher of the soul’s welfare)', 'वीतराग, सर्वज्ञ, हितोपदेशी')],
     [b('Guru', 'गुरु'), b('Inside: attachment; outside: wealth and clothes', 'भीतर राग; बाहर धन और वस्त्र'), b('Nirgranth Digambar: free of sense-desire, of arambha and parigraha; absorbed in jnana, dhyana, tapa', 'निर्ग्रंथ दिगंबर: विषयाशा, आरंभ-परिग्रह रहित; ज्ञान-ध्यान-तप में लीन')],
     [b('Dharma', 'धर्म'), b('Includes himsa', 'हिंसा सहित'), b('Ahimsa as its root; taught by the Jinas', 'अहिंसा मूल; जिनेन्द्र-कथित')],
     [b('Shastra', 'शास्त्र'), b('Ekant, supporting sense pleasure, written by the passionate', 'एकांत, विषय-पोषक, रागी-रचित'), b('Anekant, leading to vairagya, from the Sarvajna through the Acharyas', 'अनेकांत, वैराग्य-वर्धक, सर्वज्ञ से आचार्य-परंपरा द्वारा आगत')]])

d2_intro = ('<div class="card">' + bd(
  'Dhal 2 explains <b>what stands in the way</b>: Mithyatva (wrong faith, knowledge and conduct). Each has two kinds: <b>Agrihit</b> (innate, present from beginningless time) and <b>Grihit</b> (picked up from false teachers in this life). The tree below is the map of the Dhal: every verse fits somewhere on it.',
  'दूसरी ढाल बताती है कि <b>बाधा क्या है</b>: मिथ्यात्व (मिथ्या श्रद्धा, ज्ञान, चारित्र)। प्रत्येक के दो भेद हैं: <b>अगृहीत</b> (सहज, अनादि से) और <b>गृहीत</b> (इसी जन्म में कुगुरु आदि से ग्रहण किया)। नीचे का वृक्ष इस ढाल का मानचित्र है: हर पद इसमें कहीं बैठता है।') + TREE + '</div>')

DHAL2 = dict(
    path='chhah-dhala/dhal-2.html', title=('Chhahdhala · Second Dhal', 'छहढाला · दूसरी ढाल'),
    by=('Pt. Daulatram · Mithyatva (wrong faith, knowledge and conduct)', 'पं. दौलतराम · मिथ्यात्व (मिथ्यादर्शन, ज्ञान, चारित्र)'),
    desc='Chhahdhala second dhal: original verses, Hindi and English meaning and illustrated explanation.',
    crumbs=[('chhah-dhala/', ('Chhah Dhala', 'छहढाला'))],
    prev=('dhal-1.html', ('First Dhal', 'पहली ढाल')), next=('./', ('Chhah Dhala', 'छहढाला')),
    intro=d2_intro, foot=FOOT_OK,
    sections=[
      sec('s1', ('Three wrongs', 'तीन मिथ्यात्व'), ('The three wrongs', 'तीन मिथ्यात्व'), None, d2[0:1]),
      sec('s2', ('Agrihit darshan', 'अगृहीत दर्शन'), ('Agrihit mithyadarshan and mithyajnan: the seven tattvas', 'अगृहीत मिथ्यादर्शन और मिथ्याज्ञान: सात तत्त्व'),
          ('Each of the seven tattvas is believed wrongly. Compare the wrong and the right belief in the table.', 'सातों तत्त्वों में विपरीत श्रद्धा होती है। सारणी में विपरीत और सही श्रद्धा की तुलना देखें।'), d2[1:7], TATTVA_TABLE),
      sec('s3', ('Agrihit charitra', 'अगृहीत चारित्र'), ('Agrihit mithyacharitra', 'अगृहीत मिथ्याचारित्र'), None, d2[7:8]),
      sec('s4', ('Grihit darshan', 'गृहीत दर्शन'), ('Grihit mithyadarshan: false Dev, Guru, Dharma', 'गृहीत मिथ्यादर्शन: कुदेव, कुगुरु, कुधर्म'),
          ('Compare the false with the true in the table, as taught in the Digambar tradition.', 'सारणी में दिगंबर परंपरा के अनुसार झूठे और सच्चे की तुलना देखें।'), d2[8:12], TRUE_FALSE),
      sec('s5', ('Grihit jnan, charitra', 'गृहीत ज्ञान, चारित्र'), ('Grihit mithyajnana, mithyacharitra and the call', 'गृहीत मिथ्याज्ञान, मिथ्याचारित्र और आह्वान'), None, d2[12:15]),
    ])

# ======================= HUB =======================
def tile(href, en, hi, sub_en, sub_hi, tag_en, tag_hi, soon=False):
    inner = f'<h3>{b(en, hi)}</h3><p>{b(sub_en, sub_hi)}</p><span class="tag">{b(tag_en, tag_hi)}</span>'
    return f'<div class="tile soon">{inner}</div>' if soon else f'<a class="tile" href="{href}">{inner}</a>'

hub_tiles = '<div class="hub">' + ''.join([
    tile('dhal-1.html', 'First Dhal', 'पहली ढाल', 'Sansar-dukh: suffering in the four gatis', 'संसार के दुःख: चारों गतियों में', 'Open →', 'खोलें →'),
    tile('dhal-2.html', 'Second Dhal', 'दूसरी ढाल', 'Mithyatva: wrong faith, knowledge, conduct', 'मिथ्यात्व: मिथ्या श्रद्धा, ज्ञान, चारित्र', 'Open →', 'खोलें →'),
    tile('', 'Third Dhal', 'तीसरी ढाल', 'Samyagdarshan and the path of liberation', 'सम्यग्दर्शन और मोक्षमार्ग', 'Coming soon', 'जल्द आ रहा है', True),
    tile('', 'Fourth Dhal', 'चौथी ढाल', 'Samyagjnan and the vows of the householder', 'सम्यग्ज्ञान और श्रावक के व्रत', 'Coming soon', 'जल्द आ रहा है', True),
    tile('', 'Fifth Dhal', 'पाँचवीं ढाल', 'The twelve Bhavanas (Anupreksha)', 'बारह भावना (अनुप्रेक्षा)', 'Coming soon', 'जल्द आ रहा है', True),
    tile('', 'Sixth Dhal', 'छठी ढाल', 'Muni dharma, Arihant, Siddha, Moksha', 'मुनि धर्म, अरिहंत, सिद्ध, मोक्ष', 'Coming soon', 'जल्द आ रहा है', True),
]) + '</div>'

hub_flow = flow([fbox('1. Suffering of the cycle', '१. संसार का दुःख', 'red'), arrow('rd'),
                 fbox('2. Its cause: mithyatva', '२. कारण: मिथ्यात्व', 'gold'), arrow('rd'),
                 fbox('3. Cure: samyagdarshan and Ratnatraya', '३. उपाय: सम्यग्दर्शन, रत्नत्रय', 'acc'), arrow('rd'),
                 fbox('4–5. Knowledge, vows, vairagya', '४–५. ज्ञान, व्रत, वैराग्य', 'teal'), arrow('rd'),
                 fbox('6. Muni dharma and Moksha', '६. मुनि धर्म और मोक्ष', 'green')])

HUB = dict(
    path='chhah-dhala/index.html', title=('Chhah Dhala', 'छहढाला'),
    by=('Pt. Daulatram · six chapters (Dhals) on the path of liberation', 'पं. दौलतराम · मोक्षमार्ग पर छह ढालें'),
    desc='Chhahdhala of Pt. Daulatram: original verses with Hindi and English explanation.',
    crumbs=[('chhah-dhala/', ('Chhah Dhala', 'छहढाला'))],
    foot=FOOT_OK,
    sections=[dict(id='about', nav=('About', 'परिचय'), title=('About the Chhahdhala', 'छहढाला परिचय'), intro=None, units=[],
        diagram='<div class="card">' + bd(
          'The <b>Chhahdhala</b> (“six Dhals”) is a short poem by <b>Pt. Daulatram</b>, a householder-poet of the 19th century, in simple Hindi (Braj) verse. It teaches the whole path in six chapters and is recited and memorised in Digambar Jain schools and homes. <b>Each page here gives:</b> the original verse, its meaning in Hindi and English, a plain-language explanation, key words and diagrams.',
          '<b>छहढाला</b> (“छह ढालें”) 19वीं शताब्दी के गृहस्थ-कवि <b>पं. दौलतराम</b> की सरल हिन्दी (ब्रज) में रचित लघु काव्य-कृति है। यह छह अध्यायों में पूरा मार्ग सिखाती है और दिगंबर जैन पाठशालाओं तथा घरों में पढ़ी और कंठस्थ की जाती है। <b>यहाँ हर पृष्ठ पर:</b> मूल पद, हिन्दी और अंग्रेज़ी अर्थ, सरल व्याख्या, शब्दार्थ और चित्र।') + '</div>'
        + '<h3>' + b('The six Dhals at a glance', 'छह ढाल एक नज़र में') + '</h3>' + hub_flow + hub_tiles)])

PAGES = [HUB, DHAL1, DHAL2]

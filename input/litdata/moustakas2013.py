"""
Moustakas, et al. 2013, ApJ, 767, 50

For smf_tot, values are corrected as seen in Behroozi et al. 2013 (http://arxiv.org/abs/1207.6105), for D (Dust model) corrections.
"""

import numpy as np

info = \
{
 'reference':'Moustakas, et al. 2013, ApJ, 767, 50',
 'data': 'Table 3', 
 'imf': ('chabrier', (0.1, 100.)), #didn't update this
}

redshifts = [0.10165, 0.25, 0.35, 0.45, 0.575, 0.725, 0.9]
wavelength = 1600. #mulit-wavelength

ULIM = -1e10 #or this

fits = {}


tmp_data = {}
tmp_data['smf_tot'] = \
{
 0.10165: {'M': [1.7782794E+07, 2.2387211E+07, 2.8183829E+07, 3.5481339E+07, 4.4668359E+07, 5.6234133E+07, 7.0794578E+07, 8.9125094E+07, 1.1220185E+08,
           1.4125375E+08, 1.7782794E+08, 2.2387211E+08, 2.8183829E+08, 3.5481339E+08, 4.4668359E+08, 5.6234133E+08, 7.0794578E+08, 8.9125094E+08,
           1.0000000E+09, 1.1220185E+09, 1.2589254E+09, 1.4125375E+09, 1.5848932E+09, 1.7782794E+09, 1.9952623E+09, 2.2387211E+09, 2.5118864E+09,
           2.8183829E+09, 3.1622777E+09, 3.5481339E+09, 3.9810717E+09, 4.4668359E+09, 5.0118723E+09, 5.6234133E+09, 6.3095734E+09, 7.0794578E+09,
           7.9432823E+09, 8.9125094E+09, 1.0000000E+10, 1.1220185E+10, 1.2589254E+10, 1.4125375E+10, 1.5848932E+10, 1.7782794E+10, 1.9952623E+10,
           2.2387211E+10, 2.5118864E+10, 2.8183829E+10, 3.1622777E+10, 3.5481339E+10, 3.9810717E+10, 4.4668359E+10, 5.0118723E+10, 5.6234133E+10,
           6.3095734E+10, 7.0794578E+10, 7.9432823E+10, 8.9125094E+10, 1.0000000E+11, 1.1220185E+11, 1.2589254E+11, 1.4125375E+11, 1.5848932E+11,
           1.7782794E+11, 1.9952623E+11, 2.2387211E+11, 2.5118864E+11, 2.8183829E+11, 3.1622777E+11, 3.5481339E+11, 3.9810717E+11, 4.4668359E+11,
           5.0118723E+11, 5.6234133E+11, 6.3095734E+11, 7.0794578E+11, 7.9432823E+11, 8.9125094E+11],
    'phi': [-0.5854599295971292, -0.8716861558976037, -0.7173968859369291, -0.7875582621696879, -0.9496803987826172, -0.9216613894081557,
           -0.9886996277302934, -1.0815807710545238, -1.1548341411453111, -1.2073573676586995, -1.3100478269355182, -1.3950694372232921,
           -1.427628053306659, -1.5975259790579128, -1.6298607755496355, -1.6482318429613698, -1.7241205088469453, -1.8006295101917111,
           -1.9108511484176507, -1.895663142327341, -1.9288252168673736, -1.958157460899148, -1.95490400916987, -1.9958549597702335,
           -2.0602930928426653, -2.066003802690538, -2.073838203930647, -2.102797515374, -2.1226620626830255, -2.129073733824808, -2.174562846488696,
           -2.1897137027364546, -2.1737949284939466, -2.1682939964873085, -2.211634331400299, -2.223743505511813, -2.214812579970638,
           -2.2461573611512806, -2.2567788155495343, -2.2674221061872095, -2.249889054557203, -2.270665090941871, -2.274013270641099,
           -2.2676762154806114, -2.2885099639000273, -2.290734280201928, -2.31199241937864, -2.3367222703701187, -2.3573722790146077,
           -2.379641126849693, -2.416086306128673, -2.4302972748683382, -2.4802599236732887, -2.528846228687042, -2.5683725222384006,
           -2.618850610478396, -2.6861369961025954, -2.756532832269793, -2.819495644680403, -2.9013389719586065, -3.0192673534800125,
           -3.12572291139217, -3.2230570437521786, -3.3564821842268513, -3.4629204642981986, -3.626630021106111, -3.783253666390025,
           -3.9442395353122652, -4.155862812924755, -4.352151684297735, -4.57798171703595, -4.8119550581837265, -4.92889157821755, -5.341206623212072,
           -5.581823047417155, -5.831649859814056, -6.164634795713889, -6.515121013034236],
    'err': [(-0.7539735237559152, -0.9849299084777864), (-1.1241083447092908, -1.3474401498291722), (-1.0307731293745324, -1.2103779595464639),
           (-1.145379262834078, -1.3131637631412632), (-1.338642993498983, -1.4998844132110927), (-1.381652473550756, -1.507936983048775),
           (-1.5000763613453685, -1.6140926101727595), (-1.6130399185382673, -1.72178423115487), (-1.7976598061383726, -1.8659681915721085),
           (-1.9432970773175833, -1.9894065524941986), (-2.097383731993717, -2.1332192162777526), (-2.246726453087777, -2.242995170400498),
           (-2.335503383937351, -2.2939966507912724), (-2.525615323182136, -2.466948548029972), (-2.6771622124273504, -2.556895477176615),
           (-2.7443588706317463, -2.5658860456629013), (-2.8761848112581663, -2.648366791438047), (-3.089408571663229, -2.7817661811874537),
           (-3.17248921653399, -3.195073823678584), (-3.1628947305508044, -3.1852038878388003), (-3.2146381280533913, -3.229855212531355),
           (-3.2591874565631294, -3.2591874565631294), (-3.255934004833851, -3.255934004833851), (-3.296884955434215, -3.296884955434215),
           (-3.3613230885066465, -3.3613230885066465), (-3.3670337983545187, -3.3670337983545187), (-3.3748681995946277, -3.3748681995946277),
           (-3.4038275110379814, -3.4038275110379814), (-3.4236920583470067, -3.4236920583470067), (-3.4301037294887893, -3.4301037294887893),
           (-3.4755928421526767, -3.4755928421526767), (-3.490743698400436, -3.490743698400436), (-3.474824924157928, -3.474824924157928),
           (-3.4693239921512897, -3.4693239921512897), (-3.51266432706428, -3.51266432706428), (-3.5247735011757944, -3.5247735011757944),
           (-3.515842575634619, -3.515842575634619), (-3.547187356815262, -3.547187356815262), (-3.5578088112135156, -3.5578088112135156),
           (-3.5684521018511908, -3.5684521018511908), (-3.5509190502211836, -3.5509190502211836), (-3.571695086605852, -3.571695086605852),
           (-3.57504326630508, -3.57504326630508), (-3.568706211144592, -3.568706211144592), (-3.5895399595640085, -3.5895399595640085),
           (-3.591764275865909, -3.591764275865909), (-3.6130224150426207, -3.6130224150426207), (-3.6377522660341, -3.6377522660341),
           (-3.658402274678589, -3.658402274678589), (-3.680671122513674, -3.680671122513674), (-3.7171163017926543, -3.7171163017926543),
           (-3.7313272705323195, -3.7313272705323195), (-3.78128991933727, -3.78128991933727), (-3.8298762243510227, -3.8298762243510227),
           (-3.869402517902382, -3.869402517902382), (-3.919880606142377, -3.919880606142377), (-3.9871669917665766, -3.9871669917665766),
           (-4.057562827933774, -4.057562827933774), (-4.120525640344384, -4.120525640344384), (-4.202368967622587, -4.202368967622587),
           (-4.320297349143994, -4.320297349143994), (-4.426752907056151, -4.426752907056151), (-4.52408703941616, -4.52408703941616),
           (-4.6575121798908325, -4.6575121798908325), (-4.76395045996218, -4.76395045996218), (-4.927660016770092, -4.927660016770092),
           (-5.084283662054006, -5.084283662054006), (-5.2452695309762465, -5.2452695309762465), (-5.456892808588736, -5.456892808588736),
           (-5.550006615479058, -5.575966555149085), (-5.651695136951839, -5.68563131155572), (-5.758697629619895, -5.80311669274306),
           (-5.806499732408108, -5.857801440123693), (-5.984891839354163, -6.067124597232311), (-6.079686189664687, -6.188492690366167),
           (-6.172659810139724, -6.317719509869866), (-6.2670428272172725, -6.485400453838671), (-6.396574131183452, -6.70621330366231)]
   },
 0.25: {'M': [6.3095734E+08, 7.9432823E+08, 1.0000000E+09, 1.2589254E+09, 1.5848932E+09, 1.9952623E+09, 2.5118864E+09, 3.1622777E+09, 3.9810717E+09,
           5.0118723E+09, 6.3095734E+09, 7.9432823E+09, 1.0000000E+10, 1.2589254E+10, 1.5848932E+10, 1.9952623E+10, 2.5118864E+10, 3.1622777E+10,
           3.9810717E+10, 5.0118723E+10, 6.3095734E+10, 7.9432823E+10, 1.0000000E+11, 1.2589254E+11, 1.5848932E+11],
    'phi': [-2.024321931331145, -2.0459611741739696, -2.0209544960991273, -2.1682025075464373, -2.112661817917846, -2.1086526923162263,
           -2.1053035423379245, -2.1106142486306907, -2.1734114780832976, -2.2095726753056546, -2.1674214780218173, -2.218360213309234,
           -2.3012637089697634, -2.253784731423799, -2.362436226588608, -2.389489949913857, -2.353516872789589, -2.4115131605396085,
           -2.4430850934485595, -2.5729912928796526, -2.65985146461637, -2.717525168959465, -2.877630097415535, -2.9159852720642983,
           -2.966029699214405],
    'err': [(-2.3943131673560454, -2.3975901891486378), (-2.577303100076499, -2.583004341023935), (-2.399818256462029, -2.406960186105639),
           (-2.5877398785355124, -2.591396614749116), (-2.585867372122597, -2.589405633359007), (-2.701684877458977, -2.709132403940765),
           (-2.699353863121836, -2.702118057844555), (-2.7636262196810377, -2.76869727618545), (-2.786520247321853, -2.7893297982659413),
           (-2.8908666751881853, -2.8947832056436047), (-2.8969985124680466, -2.9012304073518695), (-2.8142494672864737, -2.818186296287696),
           (-3.0347343428075675, -3.041116494085214), (-2.901399540766615, -2.904945955521206), (-3.001371277400503, -3.0062030970578544),
           (-3.0940414216524683, -3.1023633260072825), (-2.9729180589702526, -2.9772980529223467), (-3.0919322893619, -3.099556036124287),
           (-3.1220587506863264, -3.130203883630047), (-3.1327980643056934, -3.141799385680362), (-3.2863681568241114, -3.3028842167070116),
           (-3.1687923551595247, -3.1804975412066065), (-3.271017136875296, -3.296496260397537), (-3.1993208109428126, -3.2175506525624957),
           (-3.15083750494072, -3.24029624659529)]
   },
 0.35: {'M': [1.5848932E+09, 1.9952623E+09, 2.5118864E+09, 3.1622777E+09, 3.9810717E+09, 5.0118723E+09, 6.3095734E+09, 7.9432823E+09, 1.0000000E+10,
           1.2589254E+10, 1.5848932E+10, 1.9952623E+10, 2.5118864E+10, 3.1622777E+10, 3.9810717E+10, 5.0118723E+10, 6.3095734E+10, 7.9432823E+10,
           1.0000000E+11, 1.2589254E+11, 1.5848932E+11, 1.9952623E+11, 2.5118864E+11, 3.1622777E+11],
    'phi': [-2.1177533172365544, -2.190445671996363, -2.1728259448236193, -2.147046322627525, -2.1923878610654963, -2.239762281825771,
           -2.1604603638538076, -2.2241828289751635, -2.2408589150786757, -2.243452889409009, -2.254421687578491, -2.298749865562339,
           -2.3255412041040473, -2.3401208638416393, -2.416043289862999, -2.497780516942967, -2.5152106094571867, -2.7252950072824595,
           -2.8704808951427023, -2.9394985806932676, -3.2535900109186677, -3.368586673255745, -3.8160841789589153, -4.398820346641219],
    'err': [(-2.5505759907360246, -2.553062447763757), (-2.610087591599879, -2.612133951986881), (-2.645940487976178, -2.661053430931715),
           (-2.6722559457299955, -2.678829782489683), (-2.829991347738326, -2.831960000414945), (-2.989111363393237, -2.993239838158138),
           (-2.823449176642683, -2.8269828717152654), (-2.910488045311172, -2.912738264684832), (-2.9916166858867137, -2.9942464569129106),
           (-3.0648441567974465, -3.0716652066850405), (-3.066853580496362, -3.072484981093504), (-3.1172258588847743, -3.121296554098767),
           (-3.022426475704631, -3.024962315937931), (-3.0696672404311727, -3.0728086755149313), (-3.231229996582821, -3.2374365937202767),
           (-3.279620230780766, -3.2869255588037043), (-3.2299252038660358, -3.2370808115734864), (-3.5187620646899496, -3.537233205412177),
           (-3.5220469368800686, -3.537186374166988), (-3.64321668770628, -3.6688825903675317), (-3.854921899172606, -3.911195556652266),
           (-3.889347672332446, -3.962356076230645), (-4.060158052997443, -4.182709565338993), (-4.170750409742569, -4.346068000873422)]
   },
 0.45: {'M': [3.1622777E+09, 3.9810717E+09, 5.0118723E+09, 6.3095734E+09, 7.9432823E+09, 1.0000000E+10, 1.2589254E+10, 1.5848932E+10, 1.9952623E+10,
           2.5118864E+10, 3.1622777E+10, 3.9810717E+10, 5.0118723E+10, 6.3095734E+10, 7.9432823E+10, 1.0000000E+11, 1.2589254E+11, 1.5848932E+11,
           1.9952623E+11, 2.5118864E+11, 3.1622777E+11, 3.9810717E+11],
    'phi': [-2.291465229353381, -2.262270786379712, -2.183137870786308, -2.2386202593319977, -2.2452993252872226, -2.2680673195487815,
           -2.328804007876212, -2.309626693083941, -2.342850410873481, -2.3673574888319284, -2.3851059463168394, -2.430784150829116,
           -2.5364757955101793, -2.621949309968617, -2.7648732086689796, -2.904565617961932, -3.0853374550318846, -3.30400465389576,
           -3.6662404682055496, -3.8244186123194885, -4.089291838772964, -4.7900750120147935],
    'err': [(-2.659123324716061, -2.660104077821789), (-2.7826879133123352, -2.7938908259411313), (-2.6912842246978164, -2.711093214699736),
           (-2.8166207025249337, -2.817978538840978), (-2.916941608362701, -2.9214561964798853), (-2.913669232900501, -2.917135616242735),
           (-3.001013836545636, -3.003120893747194), (-3.0630359655304726, -3.0670664419554967), (-3.1009834149871853, -3.1066931425851783),
           (-3.0868515658582365, -3.0891196708046964), (-3.0520659769960528, -3.0544320824307256), (-3.0307255738727106, -3.032213477110085),
           (-3.1500319724297774, -3.1523061498924108), (-3.245991383146418, -3.250594318256296), (-3.509182617994127, -3.5183821445390473),
           (-3.5020990663686313, -3.510329956193756), (-3.688753453588537, -3.7037634732346696), (-3.708519377680105, -3.72322750720716),
           (-3.943088015894655, -3.9799226923723103), (-4.144869522261569, -4.24512633467429), (-4.307902933338956, -4.4425456297206605),
           (-4.546004442960204, -4.666578315496675)]
   },
 0.575: {'M': [7.9432823E+09, 1.0000000E+10, 1.2589254E+10, 1.5848932E+10, 1.9952623E+10, 2.5118864E+10, 3.1622777E+10, 3.9810717E+10, 5.0118723E+10,
           6.3095734E+10, 7.9432823E+10, 1.0000000E+11, 1.2589254E+11, 1.5848932E+11, 1.9952623E+11, 2.5118864E+11, 3.1622777E+11, 3.9810717E+11,
           6.3095734E+11],
    'phi': [-2.349182698764202, -2.316505382605155, -2.33132620236104, -2.327414527638058, -2.325603702040297, -2.3927015654915547, -2.381783450632427,
           -2.475841538996793, -2.5130880259260397, -2.6199299269361607, -2.7379953000533175, -2.891509394469856, -3.0801152880200844,
           -3.3386341390033314, -3.551588977070367, -3.7505790472813887, -4.28501761232718, -4.295920727031149, -4.902104389144725],
    'err': [(-3.001505507592503, -3.0042731018841606), (-2.9874718271490677, -2.9891325407826392), (-3.0010550708911823, -3.0030894167363194),
           (-3.0403133454371756, -3.0419427419070972), (-2.98387025850006, -2.9847078635514848), (-3.1094332031093947, -3.1104880936426813),
           (-3.0474579574780387, -3.0481485279041345), (-3.237007864024468, -3.2385016710084957), (-3.259023684538627, -3.260372602364045),
           (-3.3373603978939737, -3.3389296877391934), (-3.370601638194004, -3.3722428255740513), (-3.59105355708829, -3.5946722383376746),
           (-3.6804967718625936, -3.6853924633191224), (-3.905218493144517, -3.9163442208007697), (-4.059411368582086, -4.082652032957725),
           (-4.219383492241045, -4.279260157386472), (-4.56409320273381, -4.662370884391687), (-4.44331772889626, -4.5850085867566),
           (-4.64719814872046, -4.766050820381407)]
   },
 0.725: {'M': [1.9952623E+10, 2.5118864E+10, 3.1622777E+10, 3.9810717E+10, 5.0118723E+10, 6.3095734E+10, 7.9432823E+10, 1.0000000E+11, 1.2589254E+11,
           1.5848932E+11, 1.9952623E+11, 2.5118864E+11, 3.1622777E+11, 3.9810717E+11],
    'phi': [-2.3207502188166638, -2.3070958245756303, -2.347532215604155, -2.4031709760965114, -2.448878286789752, -2.5068990119187213,
           -2.6143579834707675, -2.8063634587277497, -2.99693171638103, -3.2513631754928656, -3.498759933557137, -3.8585909926157638,
           -4.218636744110589, -4.256460447140985],
    'err': [(-2.9987209514387363, -3.000201496113666), (-2.9296153486118106, -2.932538131677282), (-2.9427633274845424, -2.943764397967526),
           (-3.0714030521313784, -3.072780281068797), (-3.1456648543104495, -3.1469115921492796), (-3.13476718439512, -3.135720952004256),
           (-3.296510073851362, -3.2978085605724057), (-3.447034385204063, -3.4489546773903963), (-3.693250783634373, -3.697188754372064),
           (-3.878120092144591, -3.885415107478884), (-4.07324977128213, -4.084621530978558), (-4.24296009127322, -4.26654089527608),
           (-4.531547233708521, -4.6152352305427815), (-4.486005733046372, -4.62985223114139)]
   },
 0.9: {'M': [3.9810717E+10, 5.0118723E+10, 6.3095734E+10, 7.9432823E+10, 1.0000000E+11, 1.2589254E+11, 1.5848932E+11, 1.9952623E+11, 2.5118864E+11,
           3.1622777E+11, 3.9810717E+11, 5.0118723E+11, 6.3095734E+11],
    'phi': [-2.5685284798387507, -2.556333423635266, -2.655505551398078, -2.7312839930815187, -2.7934952429264053, -3.089665399280647,
           -3.2729893291297, -3.540907701387157, -3.9230975297522166, -4.464753996880118, -4.9263439579730814, -5.383463573624059, -5.305725692784991],
    'err': [(-3.150462527088947, -3.154118026878756), (-3.118348309497735, -3.1198615108579855), (-3.3417253675235625, -3.3434805814359603),
           (-3.3998696276285303, -3.4015280220833857), (-3.5466358613022884, -3.5488474369004055), (-3.7372444762612202, -3.7414335143093465),
           (-3.920879835284545, -3.9395562750251183), (-4.2402069125192625, -4.254023145745912), (-4.431837281451823, -4.461002354540237),
           (-4.906051682607332, -5.021506561161211), (-5.067937780529057, -5.250856082057358), (-5.222750846392336, -5.470956489830344),
           (-5.162909797227158, -5.421998711721451)]
   },
}

# # Table 3
tmp_data['smf_sf'] = {}#\
# {
#  0.1: {'M': list(10**np.arange(9.0, 12.1, 0.1)),
#      'phi': [-2.026,  -2.026,  -2.129,  -2.201,  -2.211,  -2.272,  -2.313,  -2.362,  -2.371,  -2.4120, 
#              -2.4450, -2.4700, -2.5240, -2.5410, -2.6090, -2.6600, -2.7370, -2.8110, -2.9340, -3.0770, 
#              -3.2500, -3.4720, -3.769, -4.102, -4.487, -4.930, -5.437, -5.98, -6.30, -6.77, -7.09],
#      'err': [(0.018, 0.017), (0.017, 0.016), (0.015, 0.015), (0.014, 0.014), (0.014, 0.013), (0.012, 0.012),
#              (0.012, 0.012), (0.011, 0.011), (0.011, 0.011), (0.0092, 0.0090), (0.0090, 0.0088), (0.0079, 0.0078),
#              (0.0074, 0.0072), (0.0071, 0.0070), (0.0066, 0.0065), (0.0063, 0.0062), (0.0062, 0.0061), (0.0059, 0.0059),
#              (0.0061, 0.0060), (0.0064, 0.0063), (0.0071, 0.0070), (0.0085, 0.0084), (0.011, 0.010), (0.016, 0.015),
#              (0.024, 0.023), (0.042, 0.038), (0.079, 0.067), (0.20, 0.10), (0.30, 0.20), (0.60, 0.30), (1.00, 0.40)],
#     },
# }


tmp_data['smf_q'] = {}#\
# {
#  0.1: {'M': list(10**np.arange(9.00, 12.1, 0.1)),
#      'phi': [-1.889,  -1.923,  -1.970,  -2.031,  -2.055,  -2.106,  -2.144,  -2.179,  -2.188,  -2.2160, 
#              -2.2340, -2.2350, -2.2620, -2.2520, -2.2850, -2.3170, -2.3650, -2.4190, -2.5040, -2.6070, 
#              -2.7280, -2.8880, -3.1040, -3.3320, -3.6060, -3.953, -4.363, -4.778, -5.255, -5.87, -6.49],
#      'err': [(0.017, 0.017), (0.017, 0.016), (0.015, 0.015), (0.015, 0.014), (0.014, 0.013), (0.012, 0.012),
#              (0.012, 0.011), (0.012, 0.012), (0.010, 0.010), (0.0086, 0.0084), (0.008, 0.0078), (0.0069, 0.0068),
#              (0.0063, 0.0062), (0.0056, 0.0056), (0.0051, 0.0051), (0.0047, 0.0046), (0.0044, 0.0044), (0.0041, 0.0041),
#              (0.0040, 0.0040), (0.0039, 0.0039), (0.0040, 0.0040), (0.0043, 0.0043), (0.0049, 0.0048), (0.0059, 0.0059),
#              (0.0080, 0.0079), (0.012, 0.012), (0.020, 0.019), (0.033, 0.031), (0.060, 0.053), (0.10, 0.10), (0.30, 0.20)],
#     },
# }


units = {'smf_tot': 'log10', 'smf_sf': 'log10', 'smf': 'log10', 'smf_q': 'log10'}

data = {}
data['smf_tot'] = {}
data['smf_sf'] = {}
data['smf_q'] = {}
for group in ['smf_tot', 'smf_sf', 'smf_q']:
    
    for key in tmp_data[group]:
        
        if key not in tmp_data[group]:
            continue
    
        subdata = tmp_data[group]
        
        mask = []
        for element in subdata[key]['err']:
            if element == ULIM:
                mask.append(1)
            else:
                mask.append(0)
        
        mask = np.array(mask)
        
        data[group][key] = {}
        data[group][key]['M'] = np.ma.array(subdata[key]['M'], mask=mask) 
        data[group][key]['phi'] = np.ma.array(subdata[key]['phi'], mask=mask) 
        data[group][key]['err'] = tmp_data[group][key]['err']

#default is the star-forming galaxies data only
data['smf'] = data['smf_tot']
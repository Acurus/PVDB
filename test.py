import logging
import pprint

import pnvdb

logfile = 'pnvdb.log'
logging.basicConfig(filename=logfile,
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')



pp = pprint.PrettyPrinter(indent=2)

nvdb = pnvdb.Nvdb(client='pnvdb', contact='jankyr@vegvesen.no')


#pp.pprint(nvdb.status())
#obj = nvdb.objekt_type(87)
#pp.pprint(obj)
#obj = nvdb.objekt_type('belysningspunkt')
#pp.pprint(obj)
#
#pos = nvdb.posisjon(x_coordinate=269815, y_coordinate=7038165)
#pp.pprint(pos.vegreferanse)
#vegref = nvdb.vegreferanse('5000Ev6hp12m1000')
#
#pp.pprint(vegref)
#pp.pprint(vegref.fylke)
#pp.pprint(vegref.kommune)
#pp.pprint(vegref.kategori)
#pp.pprint(vegref.status)
#pp.pprint(vegref.nummer)
#pp.pprint(vegref.hp)
#pp.pprint(vegref.meter)
#pp.pprint(vegref.geometri)
#pp.pprint(vegref.xyz)
#
#
#for i in nvdb.regioner():
#    pp.pprint(i.metadata)
#    pp.pprint(i.objekt.metadata)
#    break
#
#for i in nvdb.fylker():
#    pp.pprint(i.metadata)
#    pp.pprint(i.objekt.metadata)
#    break
#
#for i in nvdb.vegavdelinger():
#    pp.pprint(i.metadata)
#    pp.pprint(i.objekt.metadata)
#    break
#
#for i in nvdb.kommuner():
#    pp.pprint(i.metadata)
#    pp.pprint(i.objekt.metadata)
#    break
#
#for i in nvdb.kontraktsomrader():
#    pp.pprint(i.metadata)
#    pp.pprint(i.objekt.metadata)
#    break
#
#for i in nvdb.riksvegruter():
#    pp.pprint(i.metadata)
#    pp.pprint(i.objekt.metadata)
#    break
#
#
#objekttyper = nvdb.objekt_typer()
#[pp.pprint(i.metadata) for i in objekttyper]
#
#
#objekttype = nvdb.objekt_type(470)
#pp.pprint(obj.i_objekt_lista())
#pp.pprint(objekttype)
#pp.pprint(objekttype.barn)
#pp.pprint(objekttype.foreldre)
#pp.pprint(objekttype.metadata)
#pp.pprint(objekttype.relasjonstyper)
#pp.pprint(objekttype.styringsparametere)
#pp.pprint(objekttype.egenskapstyper)
#pp.pprint(objekttype.egenskapstype(3779))
#
#for i in objekttype.foreldre:
#    pp.pprint(i.metadata)
#    break
#pp.pprint(objekttype.dump(file_format='xml'))
#
#
#objekt = nvdb.objekt(67, 89204552)
#objekt = nvdb.objekt('tunnelløp', 89204552)
#pp.pprint(objekt)
#pp.pprint(objekt.barn)
#pp.pprint(objekt.egenskap(1081))
#pp.pprint(objekt.egenskap(1081)['verdi'])  # Navn
#pp.pprint(objekt.egenskap(1083))  # Finnes ikke
#pp.pprint(objekt.metadata.keys())
#pp.pprint(objekt.egenskaper[0].keys())
#pp.pprint(objekt.vegreferanser)
#
#
#
#
#pp.pprint(objekt.egengeometri)
#pp.pprint(objekt.geometri)
#pp.pprint(objekt.barn)
#pp.pprint(objekt.dump(file_format='xml'))
#
#omradefilter = {'fylke': '2'}
#objekter = nvdb.hent(581, omradefilter)
#for i in objekter:
#    for egenskap in i.egenskaper:
#        if egenskap['id'] == 5225:
#            pp.pprint(egenskap['verdi'])
#            break
#    break
#
#
## Should return no result
#criteria = {'kommune': '0828', 'egenskap': '1820>=20'}
#
#obj = nvdb.hent(45, criteria)
#pp.pprint(obj)
#
#criteria = {'fylke': '2', 'egenskap': '1820>=20'}  # 1820 = "Takst liten bil"
#obj = nvdb.hent(45, criteria)
#pp.pprint(obj)
#
#for i in obj:
#    pp.pprint(i)
#
#for i in obj:
#    for egenskap in i.egenskaper:
#        if egenskap['id'] == 1078:  # 1078 = "Navn bomstasjon"
#            pp.pprint(egenskap['verdi'])
#            break
#    break
#print(pnvdb.__version__)


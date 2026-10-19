# Longevity hub sayfasını DE/ES/FR olarak üretir (EN şablonunun birebir yapısı).
import re, json, html
BASE = 'https://vivelong.com'
ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>'
FAV = re.search(r'<link rel="icon"[^>]*>', open('en/what-is-longevity/index.html', encoding='utf-8').read()).group(0)
SRC = ('<a href="https://doi.org/10.1001/jamanetworkopen.2018.3605" target="_blank" rel="noopener noreferrer">Mandsager et al., JAMA Netw Open 2018</a> · '
       '<a href="https://doi.org/10.1056/NEJMoa1800389" target="_blank" rel="noopener noreferrer">Estruch et al., PREDIMED, NEJM 2018</a> · '
       '<a href="https://doi.org/10.5665/sleep.4716" target="_blank" rel="noopener noreferrer">Watson et al., Sleep 2015</a> · '
       '<a href="https://doi.org/10.1371/journal.pmed.1000316" target="_blank" rel="noopener noreferrer">Holt-Lunstad et al., PLoS Med 2010</a> · '
       '<a href="https://doi.org/10.1073/pnas.0407162101" target="_blank" rel="noopener noreferrer">Epel et al., PNAS 2004</a> · '
       '<a href="https://doi.org/10.1001/jamainternmed.2014.8187" target="_blank" rel="noopener noreferrer">Laukkanen et al., JAMA Intern Med 2015</a>')
EN = '(EN)'

LANGS = {}

LANGS['de'] = dict(
 slug='de/was-ist-longevity', loc='de_DE', author='Vivelong Redaktion',
 title='Was ist Longevity? Lebensspanne, Gesundheitsspanne und die Wissenschaft vom langen Leben | Vivelong',
 desc='Was bedeutet Longevity? Der Unterschied zwischen Lebensspanne und Gesundheitsspanne sowie die fünf evidenzbasierten Säulen: Bewegung, Ernährung, Schlaf, soziale Bindungen und Stress.',
 ogtitle='Was ist Longevity? Lebensspanne, Gesundheitsspanne und die Wissenschaft vom langen Leben',
 h1='Was ist Longevity? Die Wissenschaft vom längeren und besseren Leben',
 headline='Was ist Longevity? Die Wissenschaft vom längeren und besseren Leben',
 home='Startseite', crumb='Was ist Longevity', tag='Ratgeber · Longevity · 9 Min. Lesezeit',
 by=('Von','Veröffentlicht','Aktualisiert'),
 stats=[('Lebensspanne ≠ Gesundheit','Longevity heißt nicht nur lange leben, sondern diese Jahre gut leben'),('5 Säulen','Bewegung, Ernährung, Schlaf, soziale Bindungen, Stress'),('≥ 7 Stunden','Konsensempfehlung für den Schlaf Erwachsener (Watson 2015)')],
 note='Hinweis: Die mit (EN) gekennzeichneten Links führen zu englischsprachigen Seiten; diese Artikel liegen noch nicht auf Deutsch vor.',
 sections=[
  ('Was ist Longevity? Die kurze Antwort', [
   '<strong>Longevity bezeichnet die Länge eines langen und gesunden Lebens.</strong> Kurz gesagt geht es nicht nur darum, wie viele Jahre Sie leben, sondern wie viele davon frei von schweren Erkrankungen und Einschränkungen sind. Die Wissenschaft nennt dieses Ziel „Gesundheitsspanne“ (Healthspan).',
   'Die heutige Longevity-Forschung untersucht die Biologie des Alterns (Zellschäden, Entzündungen, Mitochondrienfunktion, Telomere) und die Möglichkeiten, sie durch den Lebensstil zu beeinflussen.']),
  ('Lebensspanne und Gesundheitsspanne: Was ist der Unterschied?', [
   'Diese Begriffe werden oft verwechselt:',
   ('ul', ['<b>Lebensspanne:</b> Die Gesamtzeit von der Geburt bis zum Tod.',
           '<b>Gesundheitsspanne:</b> Der Teil des Lebens ohne schwere Krankheit oder Pflegebedürftigkeit. Die Weltgesundheitsorganisation erfasst ihn mit dem Indikator „gesunde Lebenserwartung“.',
           '<b>Longevity:</b> Zielt auf beides: lange leben und diese Jahre gut leben.',
           '<b>Biologisches Alter:</b> Wie stark Ihre Zellen und Organe beansprucht sind, unabhängig vom Kalenderalter. <a href="/en/blog/lower-your-biological-age/">Das biologische Alter zu senken</a> ' + EN + ' ist ein gemeinsames Ziel der Longevity-Forschung.'])]),
  ('Die 5 evidenzbasierten Säulen der Longevity', [
   'Beobachtungsstudien und klinische Studien bringen ein langes, gesundes Leben am häufigsten mit den folgenden fünf Bereichen in Verbindung. Sie senken das Risiko; eine Garantie für die Lebensdauer sind sie nicht.']),
  ('1. Bewegung und kardiorespiratorische Fitness', [
   'Eine Studie von Mandsager und Kollegen, die mehr als 120.000 Menschen begleitete, berichtete, dass eine höhere kardiorespiratorische Fitness mit einer geringeren Sterblichkeit einherging – ohne erkennbare Obergrenze des Nutzens. <a href="/en/blog/vo2-max/">VO2max</a> ' + EN + ', das Maß dieser Fitness, gehört zu den meistdiskutierten Longevity-Markern. Auch Kraft zählt: <a href="/en/blog/grip-strength/">Griffkraft</a> ' + EN + ' ist ein einfacher Marker der Alternsforschung.',
   'Die Weltgesundheitsorganisation empfiehlt mindestens 150–300 Minuten moderate Ausdaueraktivität pro Woche und Muskelkräftigung an mindestens zwei Tagen. Siehe den <a href="/en/guide/movement-and-exercise/">Ratgeber Bewegung und Training</a> ' + EN + '.']),
  ('2. Ernährung: Was ist Longevity-Ernährung?', [
   'Longevity-Ernährung bedeutet ein Essmuster, das auf langfristige Gesundheit zielt: überwiegend pflanzlich und arm an ultraverarbeiteten Lebensmitteln. Einer der stärksten Studienbelege ist PREDIMED: Eine mediterrane Kost, ergänzt durch Olivenöl oder Nüsse, senkte bei Menschen mit hohem Herz-Kreislauf-Risiko schwere kardiovaskuläre Ereignisse.',
   'Auch der Zeitpunkt der Mahlzeiten wird erforscht: <a href="/en/blog/circadian-eating/">zirkadiane Ernährung</a> ' + EN + ' und <a href="/en/blog/autophagy/">Autophagie</a> ' + EN + ' sind Themen dieses Feldes. Siehe den <a href="/en/guide/longevity-nutrition/">Ratgeber Longevity-Ernährung</a> ' + EN + '.']),
  ('3. Schlaf', [
   'Eine Konsenserklärung der American Academy of Sleep Medicine und der Sleep Research Society besagt, dass Erwachsene regelmäßig mindestens 7 Stunden schlafen sollten, um gesund zu bleiben. Chronischer Schlafmangel wird mit metabolischen und kardiovaskulären Risiken sowie mit Markern zellulären Stresses in Verbindung gebracht. Siehe den <a href="/en/guide/sleep-and-mental-health/">Ratgeber Schlaf und mentale Gesundheit</a> ' + EN + '.']),
  ('4. Soziale Bindungen und Lebenssinn', [
   'Eine Metaanalyse von Holt-Lunstad und Kollegen, die 148 Studien (rund 308.000 Teilnehmende) zusammenfasste, fand, dass Menschen mit stärkeren sozialen Beziehungen eine etwa 50 Prozent höhere Überlebenswahrscheinlichkeit hatten. Starke soziale Netze sind auch in den langlebigen Gemeinschaften der Welt verbreitet: <a href="/en/blog/power-9-blue-zones/">Power 9 und Blue Zones</a> ' + EN + ' sowie <a href="/en/blue-zones/okinawa/">Okinawa</a> ' + EN + '. Siehe den <a href="/en/guide/social-connection-and-purpose/">Ratgeber soziale Bindungen und Lebenssinn</a> ' + EN + '.']),
  ('5. Stressbewältigung und Zellalterung', [
   'Eine Studie von Epel und Kollegen aus dem Jahr 2004 brachte anhaltend hohen wahrgenommenen Stress mit kürzeren <a href="/en/blog/telomeres/">Telomeren</a> ' + EN + ' in Verbindung. Das ist ein Zusammenhang, kein Beweis für Ursächlichkeit, weist aber auf eine Verbindung zwischen Stress und biologischem Altern hin. Die Gesundheit der <a href="/en/blog/mitochondria/">Mitochondrien</a> ' + EN + ' und Entzündungen (Inflammaging) gehören zur selben Geschichte.']),
  ('Rapamycin, Sauna und andere Interventionen: Wie gut ist die Evidenz?', [
   'In der Longevity-Szene erhalten weitere Themen Aufmerksamkeit. Entscheidend ist, die Evidenzstufen zu unterscheiden:',
   ('ul', ['<b>Rapamycin:</b> Verlängert nachweislich die Lebensdauer von Mäusen; die Evidenz für die Langlebigkeit beim Menschen reicht nicht aus. <a href="/en/blog/rapamycin-and-longevity/">Details</a> ' + EN + '.',
           '<b>Sauna:</b> In einer finnischen Beobachtungsstudie ging häufige Saunanutzung mit geringerer kardiovaskulärer und Gesamtsterblichkeit einher (Laukkanen 2015); als Beobachtungsstudie kann sie Ursache und Wirkung nicht belegen. <a href="/en/blog/sauna-and-longevity/">Details</a> ' + EN + '.',
           '<b>Vertiefen:</b> <a href="/en/blog/how-to-increase-vo2-max/">How to Increase VO2 Max</a> ' + EN + ', <a href="/en/blog/what-is-a-good-vo2-max/">What Is a Good VO2 Max?</a> ' + EN + ', <a href="/en/blog/how-to-lengthen-telomeres/">How to Lengthen Telomeres</a> ' + EN + ', <a href="/en/blog/sauna-benefits-and-risks/">Sauna Benefits and Risks</a> ' + EN + '.',
           '<b>Nahrungsergänzungsmittel und Medikamente:</b> Sollten nicht ohne ärztliche Begleitung begonnen werden.'])]),
 ],
 faq_h='Häufig gestellte Fragen',
 faq=[('Was ist Longevity?','Longevity bezeichnet die Länge eines langen und gesunden Lebens. Es geht nicht nur darum, wie lange Sie leben, sondern wie viele dieser Jahre frei von schweren Erkrankungen und Einschränkungen sind – in der Wissenschaft Gesundheitsspanne genannt.'),
      ('Was bedeutet Longevity?','Longevity bedeutet Langlebigkeit oder langes Leben. Heute bezeichnet der Begriff auch das Forschungsfeld, das die Biologie des Alterns und das gesunde Altern untersucht.'),
      ('Was ist der Unterschied zwischen Lebensspanne und Gesundheitsspanne?','Die Lebensspanne ist die Gesamtzeit von der Geburt bis zum Tod. Die Gesundheitsspanne ist der Teil dieser Zeit, der ohne schwere Krankheit oder Abhängigkeit gelebt wird. Longevity zielt auf beides.'),
      ('Was ist Longevity-Ernährung?','Ein Essmuster, das auf langfristige Gesundheit zielt, überwiegend pflanzlich und arm an ultraverarbeiteten Lebensmitteln. In der PREDIMED-Studie senkte eine mediterrane Kost mit Olivenöl oder Nüssen kardiovaskuläre Ereignisse.'),
      ('Welche Gewohnheiten sind für ein langes Leben am wichtigsten?','Die Forschung hebt regelmäßige Bewegung und Fitness, ausgewogene Ernährung, ausreichend Schlaf (mindestens 7 Stunden bei Erwachsenen), starke soziale Bindungen und Stressbewältigung hervor. Sie senken das Risiko, garantieren aber keine Lebensdauer.'),
      ('Was ist das biologische Alter und wie hängt es mit Longevity zusammen?','Das biologische Alter beschreibt, wie stark Ihre Zellen und Organe beansprucht sind, unabhängig vom Kalenderalter. Die Longevity-Forschung will das biologische Altern verlangsamen und gesunde Lebensjahre verlängern.')],
 src_label='Quellen', disclaimer='<strong>Dieser Inhalt dient ausschließlich der Information und ist keine medizinische Beratung oder Behandlung.</strong> Besprechen Sie Entscheidungen zu Ihrer Gesundheit immer mit einer Ärztin oder einem Arzt. Vivelong stellt keine medizinische Diagnose und bietet keine Behandlung an.',
 related_h='Mehr aus Blog & Forschung (auf Englisch)', foot='← Vivelong Startseite (EN)', foot2='Entwickelt, um die Longevity-Wissenschaft allen zugänglich zu machen.',
 kvkk=dict(
  t='🔒 Datenschutzhinweis',
  intro='Dieser Hinweis wurde von <strong>Vivelong</strong> in Anlehnung an die geltenden Datenschutzgrundsätze erstellt, darunter die EU-Datenschutz-Grundverordnung (DSGVO) und das türkische Gesetz Nr. 6698 zum Schutz personenbezogener Daten.',
  secs=[('1. Verantwortlicher','p','Vivelong (vivelong.com) ist der Verantwortliche für die Datenverarbeitung.'),
        ('2. Verarbeitete personenbezogene Daten','ul',['Vor- und Nachname','E-Mail-Adresse','Forenbeiträge und Aktivität','Mitgliedsdatum und Nutzungspräferenzen']),
        ('3. Zwecke der Verarbeitung','ul',['Erstellung und Verwaltung Ihres Mitgliedskontos','Bereitstellung des Forums','E-Mail-Updates und Marketing (sofern Sie eingewilligt haben)','Durchführung des Programms „Mitglied des Monats“','Erfüllung rechtlicher Pflichten']),
        ('4. Datenübermittlung','p','Ihre personenbezogenen Daten können, nur soweit zur Erbringung des Dienstes erforderlich, an unseren Infrastrukturanbieter (Supabase – Server in der EU/den USA) und unseren E-Mail-Dienst (Brevo – Server in der EU) weitergegeben werden.'),
        ('5. Speicherdauer','p','Ihre Daten werden für die Dauer Ihrer Mitgliedschaft und einer gegebenenfalls geltenden gesetzlichen Aufbewahrungsfrist gespeichert und auf Antrag auf Schließung Ihres Kontos gelöscht.'),
        ('6. Ihre Rechte','ul',['Auskunft darüber, ob Ihre personenbezogenen Daten verarbeitet werden','Auskunft über Zweck der Verarbeitung und ob sie zweckgemäß verwendet werden','Auskunft darüber, an welche Dritten im In- oder Ausland Ihre Daten weitergegeben werden','Berichtigung unvollständiger oder unrichtiger Daten verlangen','Löschung Ihrer Daten verlangen','Widerspruch gegen eine ausschließlich automatisierte Entscheidung']),
        ('7. Kontakt','p','Für Anfragen: <strong>salihzekipehlivan@gmail.com</strong>')],
  btn='Verstanden, schließen'),
 cookie='Wir verwenden Cookies, um unsere Website zu analysieren und Ihre Erfahrung zu verbessern. Details finden Sie in unserem <a href="#" onclick="openKvkk(event)">Datenschutzhinweis</a>.', rej='Ablehnen', acc='Akzeptieren',
)

LANGS['es'] = dict(
 slug='es/que-es-la-longevidad', loc='es_ES', author='Equipo editorial de Vivelong',
 title='¿Qué es la longevidad? Esperanza de vida, años de vida saludable y la ciencia de vivir más | Vivelong',
 desc='¿Qué significa longevidad? La diferencia entre duración de la vida y años de vida saludable, y los cinco pilares con respaldo científico: movimiento, alimentación, sueño, vínculos sociales y estrés.',
 ogtitle='¿Qué es la longevidad? Esperanza de vida, años de vida saludable y la ciencia de vivir más',
 h1='¿Qué es la longevidad? La ciencia de vivir más y mejor',
 headline='¿Qué es la longevidad? La ciencia de vivir más y mejor',
 home='Inicio', crumb='¿Qué es la longevidad?', tag='Guía · Longevidad · 9 min de lectura',
 by=('Por','Publicado','Actualizado'),
 stats=[('Duración ≠ Salud','Longevidad no es solo vivir mucho, sino vivir bien esos años'),('5 pilares','Movimiento, alimentación, sueño, vínculos sociales, estrés'),('≥ 7 horas','Sueño recomendado por consenso para adultos (Watson 2015)')],
 note='Nota: los enlaces marcados con (EN) llevan a páginas en inglés; estos artículos aún no están disponibles en español.',
 sections=[
  ('¿Qué es la longevidad? La respuesta corta', [
   '<strong>La longevidad es la duración de una vida larga y saludable.</strong> En resumen, no se trata solo de cuántos años vive una persona, sino de cuántos de ellos transcurren sin enfermedades graves ni discapacidad. La ciencia llama a ese objetivo «healthspan» (años de vida saludable).',
   'Hoy la investigación sobre longevidad estudia la biología del envejecimiento (daño celular, inflamación, función mitocondrial, telómeros) y las formas en que el estilo de vida puede influir en ella.']),
  ('Duración de la vida y años de vida saludable: ¿cuál es la diferencia?', [
   'Estos términos suelen confundirse:',
   ('ul', ['<b>Duración de la vida (lifespan):</b> El tiempo total desde el nacimiento hasta la muerte.',
           '<b>Años de vida saludable (healthspan):</b> La parte de la vida sin enfermedad grave ni dependencia. La Organización Mundial de la Salud la sigue con el indicador de «esperanza de vida saludable».',
           '<b>Longevidad:</b> Busca ambas cosas: vivir mucho y vivir bien esos años.',
           '<b>Edad biológica:</b> Cuánto desgaste tienen sus células y órganos, independientemente de la edad cronológica. <a href="/en/blog/lower-your-biological-age/">Reducir la edad biológica</a> ' + EN + ' es un objetivo común de la investigación sobre longevidad.'])]),
  ('Los 5 pilares de la longevidad con respaldo científico', [
   'Los estudios observacionales y los ensayos clínicos relacionan con mayor constancia una vida larga y saludable con las cinco áreas siguientes. Reducen el riesgo; no garantizan la duración de la vida.']),
  ('1. Movimiento y capacidad cardiorrespiratoria', [
   'Un estudio de Mandsager y colaboradores que siguió a más de 120.000 personas informó de que una mayor capacidad cardiorrespiratoria se asociaba con menor mortalidad, sin un límite superior claro del beneficio. El <a href="/en/blog/vo2-max/">VO2 máx.</a> ' + EN + ', la medida de esa capacidad, es uno de los marcadores de longevidad más debatidos. La fuerza también cuenta: la <a href="/en/blog/grip-strength/">fuerza de prensión</a> ' + EN + ' es un marcador sencillo en la investigación del envejecimiento.',
   'La Organización Mundial de la Salud recomienda al menos 150–300 minutos de actividad aeróbica moderada por semana y fortalecimiento muscular al menos dos días. Consulte la <a href="/en/guide/movement-and-exercise/">guía de movimiento y ejercicio</a> ' + EN + '.']),
  ('2. Alimentación: ¿qué es la alimentación para la longevidad?', [
   'La alimentación para la longevidad es un patrón de comidas orientado a la salud a largo plazo: mayoritariamente vegetal y bajo en alimentos ultraprocesados. Una de las evidencias más sólidas en ensayos es PREDIMED: una dieta de estilo mediterráneo complementada con aceite de oliva o frutos secos redujo los eventos cardiovasculares graves en personas con alto riesgo cardiovascular.',
   'También se estudia el momento de las comidas: la <a href="/en/blog/circadian-eating/">alimentación circadiana</a> ' + EN + ' y la <a href="/en/blog/autophagy/">autofagia</a> ' + EN + ' son temas de este campo. Consulte la <a href="/en/guide/longevity-nutrition/">guía de alimentación para la longevidad</a> ' + EN + '.']),
  ('3. Sueño', [
   'Una declaración de consenso de la Academia Estadounidense de Medicina del Sueño y la Sociedad de Investigación del Sueño indica que los adultos deben dormir de forma regular al menos 7 horas para mantener una buena salud. El sueño corto crónico se asocia con riesgo metabólico y cardiovascular y con marcadores de estrés celular. Consulte la <a href="/en/guide/sleep-and-mental-health/">guía de sueño y salud mental</a> ' + EN + '.']),
  ('4. Vínculos sociales y propósito', [
   'Un metaanálisis de Holt-Lunstad y colaboradores que reunió 148 estudios (unos 308.000 participantes) encontró que las personas con relaciones sociales más fuertes tenían aproximadamente un 50 por ciento más de probabilidad de supervivencia. Las redes sociales sólidas también son habituales en las comunidades más longevas del mundo: <a href="/en/blog/power-9-blue-zones/">Power 9 y las Zonas Azules</a> ' + EN + ' y <a href="/en/blue-zones/okinawa/">Okinawa</a> ' + EN + '. Consulte la <a href="/en/guide/social-connection-and-purpose/">guía de vínculos sociales y propósito</a> ' + EN + '.']),
  ('5. Gestión del estrés y envejecimiento celular', [
   'Un estudio de 2004 de Epel y colaboradores relacionó el estrés percibido elevado y prolongado con <a href="/en/blog/telomeres/">telómeros</a> ' + EN + ' más cortos. Es una asociación, no una prueba de causalidad, pero apunta a un vínculo entre el estrés y el envejecimiento biológico. La salud <a href="/en/blog/mitochondria/">mitocondrial</a> ' + EN + ' y la inflamación (inflammaging) forman parte de la misma historia.']),
  ('Rapamicina, sauna y otras intervenciones: ¿qué evidencia hay?', [
   'Otros temas reciben atención en el ámbito de la longevidad. Lo importante es distinguir el nivel de evidencia:',
   ('ul', ['<b>Rapamicina:</b> Ha demostrado prolongar la vida de los ratones; la evidencia sobre la longevidad en humanos es insuficiente. <a href="/en/blog/rapamycin-and-longevity/">Detalles</a> ' + EN + '.',
           '<b>Sauna:</b> En un estudio observacional finlandés, el uso frecuente de sauna se asoció con menor mortalidad cardiovascular y total (Laukkanen 2015); al ser observacional, no puede demostrar causa y efecto. <a href="/en/blog/sauna-and-longevity/">Detalles</a> ' + EN + '.',
           '<b>Profundizar:</b> <a href="/en/blog/how-to-increase-vo2-max/">How to Increase VO2 Max</a> ' + EN + ', <a href="/en/blog/what-is-a-good-vo2-max/">What Is a Good VO2 Max?</a> ' + EN + ', <a href="/en/blog/how-to-lengthen-telomeres/">How to Lengthen Telomeres</a> ' + EN + ', <a href="/en/blog/sauna-benefits-and-risks/">Sauna Benefits and Risks</a> ' + EN + '.',
           '<b>Suplementos y fármacos:</b> No deben iniciarse sin supervisión médica.'])]),
 ],
 faq_h='Preguntas frecuentes',
 faq=[('¿Qué es la longevidad?','La longevidad es la duración de una vida larga y saludable. No se trata solo de cuánto se vive, sino de cuántos de esos años transcurren sin enfermedades graves ni discapacidad, lo que la ciencia llama healthspan.'),
      ('¿Qué significa longevidad?','Longevidad significa larga vida o vida larga. Hoy también designa el campo científico que estudia la biología del envejecimiento y el envejecimiento saludable.'),
      ('¿Cuál es la diferencia entre duración de la vida y años de vida saludable?','La duración de la vida es el tiempo total desde el nacimiento hasta la muerte. Los años de vida saludable son la parte de ese tiempo vivida sin enfermedad grave ni dependencia. La longevidad busca ambas cosas.'),
      ('¿Qué es la alimentación para la longevidad?','Un patrón de comidas orientado a la salud a largo plazo, mayoritariamente vegetal y bajo en alimentos ultraprocesados. En el ensayo PREDIMED, una dieta mediterránea con aceite de oliva o frutos secos redujo los eventos cardiovasculares.'),
      ('¿Qué hábitos importan más para una vida larga?','La investigación destaca el movimiento regular y la forma física, una alimentación equilibrada, dormir lo suficiente (al menos 7 horas en adultos), vínculos sociales sólidos y la gestión del estrés. Reducen el riesgo, pero no garantizan la duración de la vida.'),
      ('¿Qué es la edad biológica y cómo se relaciona con la longevidad?','La edad biológica indica cuánto desgaste tienen sus células y órganos, independientemente de la edad cronológica. El trabajo sobre longevidad busca ralentizar el envejecimiento biológico y prolongar los años saludables.')],
 src_label='Fuentes', disclaimer='<strong>Este contenido es solo informativo y no constituye consejo médico ni tratamiento.</strong> Consulte siempre a un médico antes de tomar decisiones sobre su salud. Vivelong no ofrece diagnóstico ni tratamiento médico.',
 related_h='Más de Blog e Investigación (en inglés)', foot='← Inicio de Vivelong (EN)', foot2='Creado para acercar la ciencia de la longevidad a todos.',
 kvkk=dict(
  t='🔒 Aviso de privacidad',
  intro='Este aviso ha sido elaborado por <strong>Vivelong</strong> conforme a los principios aplicables de protección de datos, incluidos el Reglamento General de Protección de Datos de la UE (RGPD) y la Ley n.º 6698 de Turquía sobre protección de datos personales.',
  secs=[('1. Responsable del tratamiento','p','Vivelong (vivelong.com) actúa como responsable del tratamiento.'),
        ('2. Datos personales tratados','ul',['Nombre y apellidos','Dirección de correo electrónico','Publicaciones en el foro y actividad de contenido','Fecha de alta y preferencias de uso de la plataforma']),
        ('3. Finalidades del tratamiento','ul',['Crear y gestionar su cuenta de miembro','Prestar el servicio de foro','Novedades por correo y marketing (cuando haya dado su consentimiento)','Gestionar el programa «Miembro del mes»','Cumplir obligaciones legales']),
        ('4. Transferencias de datos','p','Sus datos personales podrán compartirse, solo en la medida necesaria para prestar el servicio, con nuestro proveedor de infraestructura (Supabase — servidores en la UE/EE. UU.) y nuestro servicio de correo (Brevo — servidores en la UE).'),
        ('5. Plazo de conservación','p','Sus datos se conservan durante su afiliación y el plazo legal de conservación que corresponda, y se eliminan a petición de cierre de su cuenta.'),
        ('6. Sus derechos','ul',['Saber si se están tratando sus datos personales','Conocer la finalidad del tratamiento y si se usan conforme a ella','Conocer a qué terceros, en el país o en el extranjero, se transmiten sus datos','Solicitar la rectificación de datos incompletos o inexactos','Solicitar la supresión de sus datos','Oponerse a una decisión adoptada únicamente mediante tratamiento automatizado']),
        ('7. Contacto','p','Para solicitudes: <strong>salihzekipehlivan@gmail.com</strong>')],
  btn='Entendido, cerrar'),
 cookie='Usamos cookies para analizar nuestro sitio y mejorar su experiencia. Consulte nuestro <a href="#" onclick="openKvkk(event)">Aviso de privacidad</a> para más detalles.', rej='Rechazar', acc='Aceptar',
)

LANGS['fr'] = dict(
 slug='fr/qu-est-ce-que-la-longevite', loc='fr_FR', author='Équipe éditoriale Vivelong',
 title='Qu’est-ce que la longévité ? Durée de vie, espérance de vie en bonne santé et science du vieillissement | Vivelong',
 desc='Que signifie longévité ? La différence entre durée de vie et espérance de vie en bonne santé, et les cinq piliers fondés sur les preuves : mouvement, alimentation, sommeil, liens sociaux et stress.',
 ogtitle='Qu’est-ce que la longévité ? Durée de vie, espérance de vie en bonne santé et science du vieillissement',
 h1='Qu’est-ce que la longévité ? La science pour vivre plus longtemps et mieux',
 headline='Qu’est-ce que la longévité ? La science pour vivre plus longtemps et mieux',
 home='Accueil', crumb='Qu’est-ce que la longévité', tag='Guide · Longévité · 9 min de lecture',
 by=('Par','Publié le','Mis à jour le'),
 stats=[('Durée ≠ Santé','La longévité, ce n’est pas seulement vivre longtemps, mais bien vivre ces années'),('5 piliers','Mouvement, alimentation, sommeil, liens sociaux, stress'),('≥ 7 heures','Sommeil recommandé par consensus pour les adultes (Watson 2015)')],
 note='Remarque : les liens marqués (EN) mènent à des pages en anglais ; ces articles ne sont pas encore disponibles en français.',
 sections=[
  ('Qu’est-ce que la longévité ? La réponse courte', [
   '<strong>La longévité désigne la durée d’une vie longue et en bonne santé.</strong> En bref, il ne s’agit pas seulement du nombre d’années vécues, mais du nombre d’entre elles sans maladie grave ni incapacité. La science appelle cet objectif « healthspan » (espérance de vie en bonne santé).',
   'Aujourd’hui, la recherche sur la longévité étudie la biologie du vieillissement (dommages cellulaires, inflammation, fonction mitochondriale, télomères) et les moyens d’agir dessus par le mode de vie.']),
  ('Durée de vie et espérance de vie en bonne santé : quelle différence ?', [
   'Ces termes sont souvent confondus :',
   ('ul', ['<b>Durée de vie (lifespan) :</b> Le temps total de la naissance à la mort.',
           '<b>Espérance de vie en bonne santé (healthspan) :</b> La part de la vie passée sans maladie grave ni dépendance. L’Organisation mondiale de la santé la suit avec l’indicateur « espérance de vie en bonne santé ».',
           '<b>Longévité :</b> Vise les deux : vivre longtemps et bien vivre ces années.',
           '<b>Âge biologique :</b> Le degré d’usure de vos cellules et de vos organes, indépendamment de l’âge civil. <a href="/en/blog/lower-your-biological-age/">Réduire l’âge biologique</a> ' + EN + ' est un objectif commun des travaux sur la longévité.'])]),
  ('Les 5 piliers de la longévité fondés sur les preuves', [
   'Les études observationnelles et les essais cliniques associent le plus régulièrement une vie longue et en bonne santé aux cinq domaines ci-dessous. Ils réduisent le risque ; ils ne garantissent pas la durée de vie.']),
  ('1. Mouvement et condition cardiorespiratoire', [
   'Une étude de Mandsager et ses collègues, suivant plus de 120 000 personnes, a rapporté qu’une meilleure condition cardiorespiratoire était associée à une mortalité plus faible, sans limite supérieure nette du bénéfice. La <a href="/en/blog/vo2-max/">VO2 max</a> ' + EN + ', mesure de cette condition, est l’un des marqueurs de longévité les plus débattus. La force compte aussi : la <a href="/en/blog/grip-strength/">force de préhension</a> ' + EN + ' est un marqueur simple utilisé dans la recherche sur le vieillissement.',
   'L’Organisation mondiale de la santé recommande au moins 150 à 300 minutes d’activité aérobie modérée par semaine et un renforcement musculaire au moins deux jours. Voir le <a href="/en/guide/movement-and-exercise/">guide mouvement et exercice</a> ' + EN + '.']),
  ('2. Alimentation : qu’est-ce que l’alimentation pour la longévité ?', [
   'L’alimentation pour la longévité est un modèle alimentaire visant la santé à long terme : majoritairement végétal et pauvre en produits ultra-transformés. L’une des preuves d’essai les plus solides est PREDIMED : un régime de type méditerranéen complété par de l’huile d’olive ou des fruits à coque a réduit les événements cardiovasculaires majeurs chez des personnes à haut risque cardiovasculaire.',
   'Le moment des repas est aussi étudié : l’<a href="/en/blog/circadian-eating/">alimentation circadienne</a> ' + EN + ' et l’<a href="/en/blog/autophagy/">autophagie</a> ' + EN + ' sont des sujets de ce domaine. Voir le <a href="/en/guide/longevity-nutrition/">guide de l’alimentation pour la longévité</a> ' + EN + '.']),
  ('3. Sommeil', [
   'Une déclaration de consensus de l’American Academy of Sleep Medicine et de la Sleep Research Society indique que les adultes devraient dormir régulièrement au moins 7 heures pour rester en bonne santé. Un sommeil court chronique est associé à un risque métabolique et cardiovasculaire et à des marqueurs de stress cellulaire. Voir le <a href="/en/guide/sleep-and-mental-health/">guide sommeil et santé mentale</a> ' + EN + '.']),
  ('4. Liens sociaux et sens de la vie', [
   'Une méta-analyse de Holt-Lunstad et ses collègues regroupant 148 études (environ 308 000 participants) a constaté que les personnes ayant des relations sociales plus solides avaient une probabilité de survie supérieure d’environ 50 pour cent. De solides réseaux sociaux sont aussi courants dans les communautés les plus longévives du monde : <a href="/en/blog/power-9-blue-zones/">Power 9 et Zones bleues</a> ' + EN + ' et <a href="/en/blue-zones/okinawa/">Okinawa</a> ' + EN + '. Voir le <a href="/en/guide/social-connection-and-purpose/">guide liens sociaux et sens de la vie</a> ' + EN + '.']),
  ('5. Gestion du stress et vieillissement cellulaire', [
   'Une étude de 2004 d’Epel et ses collègues a associé un stress perçu élevé et prolongé à des <a href="/en/blog/telomeres/">télomères</a> ' + EN + ' plus courts. C’est une association, pas une preuve de causalité, mais elle indique un lien entre le stress et le vieillissement biologique. La santé <a href="/en/blog/mitochondria/">mitochondriale</a> ' + EN + ' et l’inflammation (inflammaging) font partie de la même histoire.']),
  ('Rapamycine, sauna et autres interventions : où en sont les preuves ?', [
   'D’autres sujets retiennent l’attention dans le domaine de la longévité. L’essentiel est de distinguer le niveau de preuve :',
   ('ul', ['<b>Rapamycine :</b> Prolonge la durée de vie chez la souris ; les preuves chez l’humain sont insuffisantes. <a href="/en/blog/rapamycin-and-longevity/">Détails</a> ' + EN + '.',
           '<b>Sauna :</b> Dans une étude observationnelle finlandaise, une utilisation fréquente du sauna était associée à une mortalité cardiovasculaire et globale plus faible (Laukkanen 2015) ; étant observationnelle, elle ne peut pas prouver la relation de cause à effet. <a href="/en/blog/sauna-and-longevity/">Détails</a> ' + EN + '.',
           '<b>Approfondir :</b> <a href="/en/blog/how-to-increase-vo2-max/">How to Increase VO2 Max</a> ' + EN + ', <a href="/en/blog/what-is-a-good-vo2-max/">What Is a Good VO2 Max?</a> ' + EN + ', <a href="/en/blog/how-to-lengthen-telomeres/">How to Lengthen Telomeres</a> ' + EN + ', <a href="/en/blog/sauna-benefits-and-risks/">Sauna Benefits and Risks</a> ' + EN + '.',
           '<b>Compléments et médicaments :</b> Ne doivent pas être commencés sans suivi médical.'])]),
 ],
 faq_h='Questions fréquentes',
 faq=[('Qu’est-ce que la longévité ?','La longévité désigne la durée d’une vie longue et en bonne santé. Il ne s’agit pas seulement de la durée de vie, mais du nombre de ces années sans maladie grave ni incapacité, ce que la science appelle healthspan.'),
      ('Que signifie longévité ?','Longévité signifie longue vie. Aujourd’hui, le terme désigne aussi le domaine scientifique qui étudie la biologie du vieillissement et le vieillissement en bonne santé.'),
      ('Quelle est la différence entre durée de vie et espérance de vie en bonne santé ?','La durée de vie est le temps total de la naissance à la mort. L’espérance de vie en bonne santé est la part de ce temps vécue sans maladie grave ni dépendance. La longévité vise les deux.'),
      ('Qu’est-ce que l’alimentation pour la longévité ?','Un modèle alimentaire visant la santé à long terme, majoritairement végétal et pauvre en produits ultra-transformés. Dans l’essai PREDIMED, un régime méditerranéen avec huile d’olive ou fruits à coque a réduit les événements cardiovasculaires.'),
      ('Quelles habitudes comptent le plus pour une vie longue ?','La recherche met en avant le mouvement régulier et la condition physique, une alimentation équilibrée, un sommeil suffisant (au moins 7 heures chez l’adulte), des liens sociaux solides et la gestion du stress. Ils réduisent le risque mais ne garantissent pas la durée de vie.'),
      ('Qu’est-ce que l’âge biologique et quel lien avec la longévité ?','L’âge biologique indique le degré d’usure de vos cellules et de vos organes, indépendamment de l’âge civil. Les travaux sur la longévité visent à ralentir le vieillissement biologique et à prolonger les années en bonne santé.')],
 src_label='Sources', disclaimer='<strong>Ce contenu est fourni à titre d’information uniquement et ne constitue ni un avis médical ni un traitement.</strong> Consultez toujours un médecin avant de prendre des décisions concernant votre santé. Vivelong ne fournit ni diagnostic ni traitement médical.',
 related_h='Plus sur le blog et la recherche (en anglais)', foot='← Accueil Vivelong (EN)', foot2='Conçu pour rendre la science de la longévité accessible à tous.',
 kvkk=dict(
  t='🔒 Avis de confidentialité',
  intro='Cet avis a été rédigé par <strong>Vivelong</strong> conformément aux principes applicables de protection des données, dont le Règlement général sur la protection des données de l’UE (RGPD) et la loi turque n° 6698 relative à la protection des données personnelles.',
  secs=[('1. Responsable du traitement','p','Vivelong (vivelong.com) agit en qualité de responsable du traitement.'),
        ('2. Données personnelles traitées','ul',['Nom et prénom','Adresse e-mail','Messages du forum et activité de contenu','Date d’adhésion et préférences d’utilisation de la plateforme']),
        ('3. Finalités du traitement','ul',['Créer et gérer votre compte membre','Fournir le service de forum','Informations par e-mail et marketing (lorsque vous avez donné votre consentement)','Gérer le programme « Membre du mois »','Respecter les obligations légales']),
        ('4. Transferts de données','p','Vos données personnelles peuvent être partagées, uniquement dans la mesure nécessaire à la fourniture du service, avec notre hébergeur (Supabase — serveurs UE/États-Unis) et notre service d’e-mail (Brevo — serveurs UE).'),
        ('5. Durée de conservation','p','Vos données sont conservées pendant la durée de votre adhésion et le délai légal de conservation applicable, puis supprimées sur demande de fermeture de votre compte.'),
        ('6. Vos droits','ul',['Savoir si vos données personnelles sont traitées','Connaître la finalité du traitement et si elles sont utilisées conformément à celle-ci','Connaître les tiers, en France ou à l’étranger, auxquels vos données sont communiquées','Demander la rectification de données incomplètes ou inexactes','Demander la suppression de vos données','Vous opposer à une décision fondée exclusivement sur un traitement automatisé']),
        ('7. Contact','p','Pour toute demande : <strong>salihzekipehlivan@gmail.com</strong>')],
  btn='Compris, fermer'),
 cookie='Nous utilisons des cookies pour analyser notre site et améliorer votre expérience. Consultez notre <a href="#" onclick="openKvkk(event)">Avis de confidentialité</a> pour en savoir plus.', rej='Refuser', acc='Accepter',
)

ORDER = ['tr', 'en', 'de', 'es', 'fr']
URL = {'tr': '/longevity-nedir/', 'en': '/en/what-is-longevity/', 'de': '/de/was-ist-longevity/', 'es': '/es/que-es-la-longevidad/', 'fr': '/fr/qu-est-ce-que-la-longevite/'}
LABEL = {'tr': 'TR', 'en': 'EN', 'de': 'DE', 'es': 'ES', 'fr': 'FR'}
HREFLANG = ''.join(f'  <link rel="alternate" hreflang="{l}" href="{BASE}{URL[l]}">\n' for l in ORDER) + f'  <link rel="alternate" hreflang="x-default" href="{BASE}{URL["tr"]}">\n'

def switcher(cur):
    return '\n'.join(f'    <a class="zp-lang-switch" href="{URL[l]}" hreflang="{l}">{LABEL[l]}</a>' for l in ORDER if l != cur) + '\n'

def esc(s): return html.escape(s, quote=True)

def build(code, L):
    url = f'{BASE}/{L["slug"]}/'
    body = []
    for h2, parts in L['sections']:
        inner = ''
        for p in parts:
            if isinstance(p, tuple):
                inner += '      <ul class="zp-ul">\n' + ''.join(f'        <li>{x}</li>\n' for x in p[1]) + '      </ul>\n'
            else:
                inner += f'      <p class="zp-p">{p}</p>\n'
        body.append(f'    <div class="zp-sec">\n      <h2>{ICON}{h2}</h2>\n{inner}    </div>\n')
    faq_html = ''.join(f'      <h3 style="font-size:16px;margin:16px 0 6px;">{q}</h3>\n      <p class="zp-p">{a}</p>\n' for q, a in L['faq'])
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "@id": url + "#content", "datePublished": "2026-10-19", "dateModified": "2026-10-19",
         "author": {"@type": "Organization", "name": L['author'], "url": f"{BASE}/en/about/"},
         "headline": L['headline'], "description": L['desc'], "url": url, "inLanguage": code,
         "isPartOf": {"@id": f"{BASE}/en/#website"}, "publisher": {"@id": f"{BASE}/en/#organization"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": L['home'], "item": f"{BASE}/en/"},
            {"@type": "ListItem", "position": 2, "name": L['crumb'], "item": url}]}]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "@id": url + "#faq",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in L['faq']]}
    stats = ''.join(f'<div class="zp-st"><div class="zp-st-n">{n}</div><div class="zp-st-l">{l}</div></div>' for n, l in L['stats'])
    k = L['kvkk']
    ksec = ''
    for t, typ, c in k['secs']:
        ksec += f'    <h4>{t}</h4>\n'
        ksec += f'    <p>{c}</p>\n' if typ == 'p' else '    <ul>\n' + ''.join(f'      <li>{x}</li>\n' for x in c) + '    </ul>\n'
    en_related = [('/en/blog/telomeres/', 'Telomeres'), ('/en/blog/vo2-max/', 'VO2 max'), ('/en/blog/mitochondria/', 'Mitochondria'), ('/en/blog/autophagy/', 'Autophagy'),
                  ('/en/blog/power-9-blue-zones/', 'Power 9 and Blue Zones'), ('/en/blog/lower-your-biological-age/', 'Lower Your Biological Age'),
                  ('/en/blog/how-to-increase-vo2-max/', 'How to Increase VO2 Max'), ('/en/blog/what-is-a-good-vo2-max/', 'What Is a Good VO2 Max?'),
                  ('/en/blog/how-to-lengthen-telomeres/', 'How to Lengthen Telomeres'), ('/en/blog/sauna-benefits-and-risks/', 'Sauna Benefits and Risks')]
    related = ''.join(f'      <li><a href="{u}">{t} {EN}</a></li>\n' for u, t in en_related)
    tpl = open('en/what-is-longevity/index.html', encoding='utf-8').read()
    gtag = re.search(r'  <script>\n    window\.dataLayer.*?</script>\n  <script async src="https://www\.googletagmanager\.com[^\n]*</script>\n', tpl, re.S).group(0)
    fonts = re.search(r'  <link rel="preconnect".*?  <link rel="stylesheet" href="/assets/site\.css">\n', tpl, re.S).group(0)
    scripts = re.search(r'<script>\nfunction openKvkk.*?</script>\n', tpl, re.S).group(0)
    logo = re.search(r'<a class="zp-home-logo".*?</a>', tpl, re.S).group(0).replace('href="/en/"', 'href="/en/"')
    out = f'''<!DOCTYPE html>
<html lang="{code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(L['title'])}</title>
  <meta name="description" content="{esc(L['desc'])}">
  <meta name="author" content="{esc(L['author'])}">
  <link rel="alternate" type="application/rss+xml" title="Vivelong" href="/feed.xml">
  <link rel="canonical" href="{url}">
{HREFLANG}  {FAV}
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Vivelong">
  <meta property="og:title" content="{esc(L['ogtitle'])}">
  <meta property="og:description" content="{esc(L['desc'])}">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="{L['loc']}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{esc(L['ogtitle'])}">
  <meta name="twitter:description" content="{esc(L['desc'])}">
  <script type="application/ld+json">
{json.dumps(graph, ensure_ascii=False, indent=2)}
</script>
  <script type="application/ld+json">
{json.dumps(faq, ensure_ascii=False, indent=2)}
</script>
{gtag}{fonts}</head>
<body>
<div class="breadcrumb"><a href="/en/">{L['home']} {EN}</a> / <span>{L['crumb']}</span></div>
<div class="zone-page open" id="zp-blog1">
  <div class="zp-topbar">
    <div class="zp-topbar-left">
      {logo}
{switcher(code)}    </div>
    <span class="zp-crumb">{L['crumb']}</span>
  </div>
  <div class="zp-hero" style="background:linear-gradient(160deg,#1A4731 0%,#2D6A4F 60%,#74C69D 100%);">
    <div class="zp-hero-inner">
      <span class="zp-emoji">🌿</span>
      <h1>{L['h1']}</h1>
      <span class="zp-tag">{L['tag']}</span>
      <p class="zp-byline" style="margin:10px 0 0;font-size:13px;opacity:.85;">{L['by'][0]}: {L['author']} · {L['by'][1]}: <time datetime="2026-10-19">2026-10-19</time> · {L['by'][2]}: <time datetime="2026-10-19">2026-10-19</time></p>
      <div class="zp-stats">{stats}</div>
    </div>
  </div>
  <div class="zp-body">
    <p class="zp-p" style="font-size:13px;opacity:.8;">{L['note']}</p>
{''.join(body)}    <div class="zp-sec">
      <h2>{ICON}{L['faq_h']}</h2>
{faq_html}    </div>
    <div class="zp-src">{L['src_label']}: {SRC}</div>
    <div class="zp-disclaimer">
      <span>{L['disclaimer']}</span>
    </div>
  </div>
</div>
<div class="related-wrap"><h3>{L['related_h']}</h3><ul class="related-list">
{related}    </ul></div>
<div class="static-footer">
  <a href="/en/">{L['foot']}</a> · © 2026 Vivelong · {L['foot2']}
</div>

<div class="kvkk-overlay" id="kvkkOverlay" onclick="if(event.target===this)closeKvkk()">
  <div class="kvkk-box">
    <h3>{k['t']}</h3>
    <p>{k['intro']}</p>
{ksec}    <button class="kvkk-close-btn" onclick="closeKvkk()">{k['btn']}</button>
  </div>
</div>
<div class="cookie-banner" id="cookieBanner">
  <p>{L['cookie']}</p>
  <div class="cookie-banner-actions">
    <button class="cookie-btn cookie-reject" id="cookieReject" onclick="setCookieConsent(false)">{L['rej']}</button>
    <button class="cookie-btn cookie-accept" id="cookieAccept" onclick="setCookieConsent(true)">{L['acc']}</button>
  </div>
</div>

{scripts}</body>
</html>
'''
    import os
    os.makedirs(L['slug'], exist_ok=True)
    open(L['slug'] + '/index.html', 'w', encoding='utf-8', newline='\n').write(out)

for c, L in LANGS.items():
    build(c, L)

# TR + EN: hreflang + dil değiştirici güncelle
for path, cur in [('longevity-nedir/index.html', 'tr'), ('en/what-is-longevity/index.html', 'en')]:
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'  <link rel="alternate" hreflang="tr".*?hreflang="x-default"[^\n]*\n', HREFLANG, s, count=1, flags=re.S)
    s = re.sub(r'    <a class="zp-lang-switch"[^\n]*\n', switcher(cur), s, count=1)
    open(path, 'w', encoding='utf-8', newline='\n').write(s)

# sitemap
sm = open('sitemap.xml', encoding='utf-8').read()
if 'xmlns:xhtml' not in sm:
    sm = sm.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">')
alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{BASE}{URL[l]}"/>' for l in ORDER) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{URL["tr"]}"/>'
for l in ORDER:
    loc = f'{BASE}{URL[l]}'
    line = re.search(r'  <url><loc>' + re.escape(loc) + r'</loc>.*?</url>\n', sm)
    new = f'  <url><loc>{loc}</loc><lastmod>2026-10-19</lastmod><changefreq>monthly</changefreq><priority>0.9</priority>{alts}</url>\n'
    if line: sm = sm.replace(line.group(0), new)
    else: sm = sm.replace('</urlset>', new + '</urlset>')
open('sitemap.xml', 'w', encoding='utf-8', newline='\n').write(sm)

# llms.txt
ll = open('llms.txt', encoding='utf-8').read()
add = ('- [Was ist Longevity?](https://vivelong.com/de/was-ist-longevity/): Deutscher Leitfaden zu Longevity, Lebensspanne vs. Gesundheitsspanne und den fünf Säulen.\n'
       '- [¿Qué es la longevidad?](https://vivelong.com/es/que-es-la-longevidad/): Guía en español sobre longevidad, duración de vida vs. años saludables y los cinco pilares.\n'
       '- [Qu’est-ce que la longévité ?](https://vivelong.com/fr/qu-est-ce-que-la-longevite/): Guide en français sur la longévité, durée de vie vs. espérance de vie en bonne santé et les cinq piliers.\n')
if 'de/was-ist-longevity' not in ll:
    anchor = '- [What Is Longevity?](https://vivelong.com/en/what-is-longevity/)'
    i = ll.index(anchor); j = ll.index('\n', i) + 1
    ll = ll[:j] + add + ll[j:]
    open('llms.txt', 'w', encoding='utf-8', newline='\n').write(ll)

# ai/summary.json
sj = json.load(open('ai/summary.json', encoding='utf-8'))
def put(d):
    if isinstance(d, dict):
        if 'what_is_longevity' in d:
            d['was_ist_longevity'] = f'{BASE}{URL["de"]}'; d['que_es_la_longevidad'] = f'{BASE}{URL["es"]}'; d['qu_est_ce_que_la_longevite'] = f'{BASE}{URL["fr"]}'
            return True
        return any(put(v) for v in d.values())
    return False
put(sj)
json.dump(sj, open('ai/summary.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=2)
print('ok')

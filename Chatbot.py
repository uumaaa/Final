import re
import random
RESPUESTA_HOLA = [
"¡Hola! Soy Chato, tu asistente virtual. ¿Cómo puedo ayudarte hoy?",
"Saludos, soy Chato. ¿En qué puedo orientarte durante el proceso de admisión?",
"Hola, ¿cómo estás? Soy Chato, aquí para facilitarte la información que necesitas.",
"¡Buenas! Soy Chato, tu asistente personal. ¿En qué puedo colaborar contigo?",
"Hola, soy Chato. ¿Necesitas ayuda con la admisión a la universidad?",
"¡Hola! Soy Chato, el asistente virtual. ¿Tienes preguntas sobre la universidad?",
"Saludos, soy Chato. ¿Qué información necesitas para tu proceso de admisión?",
"¡Hola! Estoy aquí como Chato para responder tus dudas sobre la universidad.",
"Hola, ¿cómo puedo ayudarte hoy? Soy Chato, tu asistente de confianza.",
"¡Bienvenido! Soy Chato, el asistente virtual. ¿En qué puedo asistirte?",
"¡Hola! Soy Chato, ¿quieres saber más sobre nuestra universidad?",
"Saludos, soy Chato. ¿En qué fase del proceso de admisión te encuentras?",
"Hola, soy Chato. ¿Necesitas asistencia con la solicitud de admisión?",
"¡Buen día! Soy Chato, ¿cómo puedo apoyarte durante el proceso de ingreso?",
"¡Hola! ¿En qué puedo guiarte hoy? Soy Chato, tu asistente de confianza.",
"Hola, soy Chato. ¿Te gustaría conocer más detalles sobre nuestros programas académicos?",
"¡Hola! Soy Chato, ¿qué dudas tienes sobre la admisión a nuestra universidad?",
"Saludos, soy Chato. ¿Necesitas información sobre los requisitos de admisión?",
"Hola, soy Chato. Estoy aquí para resolver tus inquietudes sobre la admisión.",
"¡Hola! ¿En qué puedo ser de ayuda para tu ingreso a la universidad?"
]
RESPUESTA_PROCESO = [
"La Universidad Universidad IFAM actualmente no tiene un proceso de admisión abierto. Sin embargo, estoy aquí para responder cualquier pregunta que tengas sobre nuestros programas académicos. ¿En qué más puedo ayudarte?",
"En estos momentos, no hay ningún proceso de admisión en curso. ¿Puedo proporcionarte información sobre carreras específicas o servicios que ofrecemos?",
"Lo siento, pero por ahora no hay procesos de admisión activos. ¿Hay algo más que te interese saber sobre nuestra universidad?",
"Actualmente, estamos fuera de temporada de admisión. Sin embargo, si necesitas información sobre nuestras instalaciones o programas, estaré encantado de ayudarte.",
"Lamentablemente, el período de admisión ha concluido. Te sugiero que vuelvas a consultarnos en un par de meses para obtener detalles sobre futuros procesos. ¿Hay algo más que pueda hacer por ti?",
"No hay un proceso de admisión en curso en este momento. ¿Quisieras saber más sobre las actividades extracurriculares que ofrecemos?",
"El proceso de admisión 2023-2 comenzará pronto. Mientras tanto, puedes explorar información sobre nuestras carreras y programas en nuestra página web: ...",
"La Universidad Universidad IFAM no tiene un proceso de admisión activo en este momento. ¿Te gustaría obtener más información sobre nuestros laboratorios y recursos?",
"En este momento, no hay procesos de admisión abiertos. Sin embargo, puedo proporcionarte detalles sobre eventos universitarios y actividades académicas. ¿Te interesa algo en particular?",
"El proceso de admisión para el próximo año está en fase de planificación. Mientras tanto, ¿puedo ayudarte con información sobre nuestras becas o servicios estudiantiles?",
"Lo siento, pero actualmente no estamos aceptando solicitudes de admisión. ¿En qué más puedo asistirte hoy?",
"El proceso de admisión para el próximo ciclo académico aún no ha comenzado. ¿Quisieras obtener información sobre nuestras instalaciones deportivas?",
"Actualmente no hay un proceso de admisión en curso. ¿Te gustaría saber más sobre nuestras alianzas internacionales y oportunidades de intercambio?",
"La Universidad Universidad IFAM no tiene un proceso de admisión disponible en este momento. ¿Necesitas información sobre los requisitos de titulación o planes de estudio?",
"En este momento, no hay procesos de admisión activos. Sin embargo, ¿puedo proporcionarte detalles sobre nuestras iniciativas de investigación y proyectos?",
"Lamentablemente, no estamos llevando a cabo procesos de admisión en este momento. ¿Hay algo más que pueda hacer por ti?",
"Actualmente, no hay procesos de admisión abiertos. ¿Te gustaría obtener información sobre nuestras actividades culturales y clubes estudiantiles?",
"El proceso de admisión para el próximo semestre aún no ha sido anunciado. Mientras tanto, ¿puedo ayudarte con información sobre nuestras instalaciones de estudio?",
"¡Hola! En este momento, no hay procesos de admisión en nuestra universidad. ¿En qué más puedo asistirte?",
"¡Hola! Soy el asistente virtual de la Universidad Universidad IFAM. En este momento, no estamos llevando a cabo procesos de admisión, pero ¿hay algo más en lo que pueda ayudarte?"]

RESPUESTA_CARRERAS = [
"Explora las opciones académicas de nuestra institución, desde Escritura Creativa y Astronomía hasta Ingeniería Aeroespacial y Ciencias de Datos.",
"En nuestra institución, ofrecemos carreras únicas que abarcan desde Bellas Artes y Literatura hasta Ingeniería Química y Estadísticas Avanzadas.",
"Descubre el abanico de carreras que ofrecemos, desde Coreografía y Fotografía hasta Ingeniería Biomédica y Física Cuántica.",
"En la universdad IFAM, la diversidad académica es nuestra fortaleza. Ofrecemos carreras como Fotografía, Arquitectura, Ciencias de la Computación y Física Teórica. Descubre más sobre cada programa en nuestra página oficial: [enlace].",
"Estamos orgullosos de nuestras carreras en artes y fisicomatemáticas, desde Diseño Gráfico y Escultura hasta Ingeniería Aeroespacial y Matemáticas Puras. Obtén información detallada sobre cada programa en nuestra página de programas académicos: [enlace].",
"Saludos. Ofrecemos carreras diversas, desde Filosofía y Ballet hasta Ingeniería de Software y Estadísticas. Si deseas conocer más detalles sobre cada programa, te invito a visitar nuestra página oficial: [enlace].",
"Aquí encontrarás carreras apasionantes como Cine, Astronomía, Ciencias de la Computación y Geofísica. Para detalles específicos sobre cada programa, visita nuestra página de programas académicos: [enlace].",
"En nuestra institución, puedes explorar carreras en Artes Visuales, Danza Contemporánea, Ingeniería Civil y Ciencias Actuariales.",
"Tenemos carreras en artes y ciencias que van desde Pintura y Diseño Industrial hasta Ingeniería Biomédica y Física Médica. Descubre más sobre cada programa en nuestra página de programas académicos: [enlace].",
"En nuestra universidad, la oferta académica incluye carreras como Teatro, Escritura Creativa, Ingeniería Informática y Bioquímica",
"Nos enorgullece ofrecer carreras diversas como Fotoperiodismo, Escultura, Ingeniería Mecatrónica y Bioinformática. Explora más sobre cada programa en nuestra página de programas académicos: [enlace].",
"Ofrecemos carreras en artes y ciencias, desde Historia del Arte y Coreografía hasta Ingeniería Nuclear y Ciencias de Datos",
"En la universdad IFAM, puedes elegir entre carreras como Diseño de Moda, Poesía, Ingeniería de Redes y Estadísticas Avanzadas. Accede a información detallada sobre cada programa en nuestra página de programas académicos: [enlace].",
"En nuestra institución, la diversidad académica es impresionante. Ofrecemos carreras en Arquitectura, Música, Ingeniería Química y Matemáticas Aplicadas.",
"Estamos emocionados de ofrecer carreras como Escritura Dramática, Escultura, Ingeniería Aeroespacial y Ciencias Actuariales.",
"En nuestra universidad, encontrarás carreras que abarcan desde Danza y Fotografía hasta Ingeniería Eléctrica y Ciencias de la Computación.",
"Accede a información detallada sobre cada programa en nuestra página de programas académicos: [enlace].",
"Para obtener información detallada sobre cada programa, visita nuestra página oficial: [enlace].",
"¡Hola! Estamos orgullosos de nuestras carreras en artes y fisicomatemáticas, desde Teatro y Escultura hasta Ingeniería Civil y Matemáticas Puras.",
"Saludos. Ofrecemos carreras en Artes Visuales, Música, Ingeniería Informática y Estadísticas."
]
RESPUESTA_REQUISITOS = [
"Para ingresar a nuestra universidad, se requiere un certificado de preparatoria, una carta de recomendación y el resultado de un examen de admisión estandarizado.",
"Los requisitos generales incluyen un promedio mínimo de 8.5, certificado de bachillerato y la aprobación de nuestro examen de admisión. Te recomendamos revisar nuestra página de requisitos para más detalles: [enlace].",
"Es necesario presentar tu certificado de bachillerato, realizar un examen de admisión y completar una entrevista. Para información detallada, consulta nuestra página de requisitos en [enlace].",
"Los requisitos para la admisión varían según la carrera. Sin embargo, en términos generales, necesitarás tu certificado de preparatoria y resultados satisfactorios en nuestras pruebas de ingreso.",
"Nuestros requisitos incluyen un promedio mínimo de 8.0, certificado de bachillerato, y una carta de motivación. Para detalles específicos, te invitamos a visitar nuestra página de admisiones: [enlace].",
"La universidad tiene requisitos específicos para cada carrera. En términos generales, se espera un promedio de al menos 8.0 y resultados satisfactorios en el examen de admisión. Para más información, visita [enlace].",
"Te invitamos a revisar los requisitos detallados en nuestra página de admisiones [enlace], que incluyen certificado de bachillerato, resultados de exámenes y una carta de presentación.",
"Los requisitos para entrar varían según la carrera. Por lo general, se requiere un promedio de al menos 8.5 y la presentación de una solicitud. Para más detalles, consulta nuestra página de requisitos: [enlace].",
"Para conocer los requisitos exactos, te sugiero visitar nuestra página de admisiones [enlace]. En términos generales, se requiere un promedio mínimo de 8.0 y resultados satisfactorios en nuestras pruebas de ingreso.",
"Los requisitos varían según la carrera que elijas. Sin embargo, se espera un promedio mínimo de 8.0 y buen desempeño en nuestras pruebas de ingreso. Encuentra información detallada en nuestra página de requisitos: [enlace].",
"Para ingresar, necesitarás tu certificado de preparatoria y aprobar nuestro examen de admisión. Los requisitos exactos varían según la carrera. Visita nuestra página de admisiones para más información: [enlace].",
"Para conocer los requisitos específicos de cada carrera, te recomiendo que visites nuestra página de admisiones [enlace]. En general, se requiere un promedio mínimo de 8.5 y buen desempeño en nuestras pruebas de ingreso.",
"Los requisitos generales incluyen un promedio mínimo de 8.0, certificado de bachillerato y aprobación del examen de admisión. Consulta nuestra página de requisitos para obtener información detallada: [enlace].",
"Necesitarás tu certificado de preparatoria, resultados de exámenes y una carta de recomendación para ingresar. Puedes encontrar información específica sobre requisitos en nuestra página de admisiones: [enlace].",
"Los requisitos de admisión pueden variar según la carrera. En términos generales, se espera un promedio mínimo de 8.5 y buen desempeño en nuestras pruebas de ingreso. Obtén detalles en nuestra página de requisitos: [enlace].",
"Los requisitos varían, pero en general, necesitarás tu certificado de preparatoria y aprobar nuestro examen de admisión. Consulta nuestra página de admisiones para obtener información detallada: [enlace].",
"Te invitamos a conocer los requisitos específicos de cada carrera en nuestra página de admisiones [enlace]. En general, se espera un promedio mínimo de 8.0 y resultados satisfactorios en nuestras pruebas de ingreso.",
"Los requisitos pueden cambiar según la carrera. Un buen promedio y resultados positivos en las pruebas de admisión son comunes. Para información detallada, consulta nuestra página de requisitos: [enlace].",
"¡Hola! Puedes revisar los requisitos específicos de cada carrera en nuestra página de admisiones [enlace]. En términos generales, se requiere un promedio mínimo de 8.5 y buen desempeño en nuestras pruebas de ingreso."
"¡Hola! Para ingresar, necesitarás tu certificado de preparatoria, realizar un examen de admisión y presentar una carta de intención. Puedes encontrar detalles específicos en nuestra página de admisiones: [enlace].",
]

RESPUESTA_ADIOS = [
"¡Hasta luego! Si tienes más preguntas en el futuro, no dudes en volver. ¿En qué más puedo ayudarte?",
"¡Adiós! Si surge algo más, estoy aquí para ayudarte. ¡Que tengas un excelente día!",
"Adiós, fue un placer ayudarte. ¿Necesitas asistencia con algo más en el futuro?",
"¡Hasta pronto! Siempre estoy disponible si necesitas más información. ¿Puedo ayudarte con algo más?",
"¡Nos vemos! Siempre estoy aquí para responder a tus preguntas. ¿Hay algo más en lo que pueda ayudarte?",
"Adiós por ahora. No dudes en regresar si tienes más consultas o necesitas ayuda. ¿Hay algo más que pueda hacer por ti?",
"¡Hasta la próxima! Siempre estoy listo para ayudar. ¿Necesitas información adicional?",
"¡Adiós! Si en algún momento tienes más preguntas, estaré aquí para ayudarte. ¿Puedo hacer algo más por ti?",
"Nos despedimos por ahora. ¿Hay algo más en lo que pueda ser de ayuda?",
"¡Que tengas un buen día! Siempre estoy disponible si necesitas más información. ¿En qué más puedo ayudarte?",
"Hasta luego. Siempre estoy aquí para ayudar, así que no dudes en volver si tienes más preguntas.",
"Adiós, pero no dudes en regresar si necesitas más asistencia. ¿En qué más puedo ayudarte?",
"¡Hasta pronto! Estoy aquí para ayudarte en lo que necesites. ¿Hay algo más en lo que pueda colaborar contigo?",
"Nos vemos. Si surge alguna otra pregunta, no dudes en contactarme. ¿Puedo ayudarte con algo más antes de irte?",
"Adiós por ahora. Si necesitas más información en el futuro, no dudes en preguntar. ¿Hay algo más en lo que pueda asistirte?",
"¡Hasta la próxima! Estoy aquí para ayudarte siempre que lo necesites. ¿En qué más puedo ser de utilidad?",
"Nos despedimos por ahora. Si alguna vez necesitas más orientación, estoy aquí para ayudarte. ¿Puedo hacer algo más por ti?",
"¡Adiós! Si tienes más consultas, estaré encantado de ayudarte en el futuro. ¿Hay algo más en lo que pueda asistirte?",
"Hasta luego. Si en algún momento necesitas más información, no dudes en contactarme. ¿En qué más puedo ayudarte?",
"¡Nos vemos pronto! Siempre estoy disponible para ayudarte en lo que necesites. ¿Puedo hacer algo más por ti?"
]

RESPUESTA_INTERCAMBIOS = [    
"Sí, ofrecemos programas de intercambio estudiantil en colaboración con diversas universidades alrededor del mundo. Puedes obtener más detalles sobre destinos, requisitos y plazos en nuestra oficina de relaciones internacionales.",
"Sí, contamos con programas de intercambio estudiantil para que puedas vivir una experiencia académica en el extranjero. Puedes obtener información detallada en nuestra página web o comunicándote con la oficina de intercambio estudiantil.",
"sí ofrecemos programas de intercambio estudiantil que te permiten estudiar en universidades asociadas en diferentes países. Para conocer los detalles y requisitos, te recomiendo visitar nuestra oficina de relaciones internacionales.",
"Sí, tenemos programas de intercambio estudiantil que te brindan la oportunidad de estudiar en el extranjero. Puedes obtener información sobre destinos y requisitos en nuestra página oficial o contactando a la oficina de intercambio estudiantil.",
"Ofrecemos programas de intercambio estudiantil para que amplíes tus horizontes académicos. Revisa nuestra página web para conocer los destinos disponibles y los requisitos para participar.",
"Sí ofrecemos programas de intercambio estudiantil que te permiten estudiar en el extranjero por un periodo determinado. Puedes obtener más detalles sobre destinos y requisitos en nuestra oficina de relaciones internacionales.",
"Sí, tenemos programas de intercambio estudiantil que te permiten estudiar en universidades asociadas en diferentes países. Obtén información detallada sobre destinos y requisitos en nuestra página web o contactando a la oficina de intercambio estudiantil.",
"Contamos con programas de intercambio estudiantil para que puedas vivir una experiencia académica en el extranjero. Puedes obtener información detallada en nuestra página web o comunicándote con la oficina de intercambio estudiantil.",
"Ofrecemos programas de intercambio estudiantil que te permiten estudiar en universidades asociadas en diferentes países. Para conocer los detalles y requisitos, te recomiendo visitar nuestra oficina de relaciones internacionales.",
"Tenemos programas de intercambio estudiantil que te brindan la oportunidad de estudiar en el extranjero. Puedes obtener información sobre destinos y requisitos en nuestra página oficial o contactando a la oficina de intercambio estudiantil.",
"Sí, ofrecemos programas de intercambio estudiantil para que amplíes tus horizontes académicos. Revisa nuestra página web para conocer los destinos disponibles y los requisitos para participar.",
"Sí ofrecemos programas de intercambio estudiantil que te permiten estudiar en el extranjero por un periodo determinado. Puedes obtener más detalles sobre destinos y requisitos en nuestra oficina de relaciones internacionales.",
"Tenemos programas de intercambio estudiantil que te permiten estudiar en universidades asociadas en diferentes países. Obtén información detallada sobre destinos y requisitos en nuestra página web o contactando a la oficina de intercambio estudiantil.",
"Sí, contamos con programas de intercambio estudiantil para que puedas vivir una experiencia académica en el extranjero. Puedes obtener información detallada en nuestra página web o comunicándote con la oficina de intercambio estudiantil.",
"Ofrecemos programas de intercambio estudiantil que te permiten estudiar en universidades asociadas en diferentes países. Para conocer los detalles y requisitos, te recomiendo visitar nuestra oficina de relaciones internacionales.",
"Tenemos programas de intercambio estudiantil que te brindan la oportunidad de estudiar en el extranjero. Puedes obtener información sobre destinos y requisitos en nuestra página oficial o contactando a la oficina de intercambio estudiantil.",
"Sí, ofrecemos programas de intercambio estudiantil para que amplíes tus horizontes académicos. Revisa nuestra página web para conocer los destinos disponibles y los requisitos para participar.",
"Ofrecemos programas de intercambio estudiantil que te permiten estudiar en el extranjero por un periodo determinado. Puedes obtener más detalles sobre destinos y requisitos en nuestra oficina de relaciones internacionales.",
"¡Hola! Sí, tenemos programas de intercambio estudiantil que te permiten estudiar en universidades asociadas en diferentes países. Obtén información detallada sobre destinos y requisitos en nuestra página web o contactando a la oficina de intercambio estudiantil.",
"Saludos. Sí, contamos con programas de intercambio estudiantil para que puedas vivir una experiencia académica en el extranjero. Puedes obtener información detallada en nuestra página web o comunicándote con la oficina de intercambio estudiantil."]

RESPUESTA_BECAS = [
"Contamos con diversas opciones de becas, como becas académicas, deportivas y de mérito. Puedes obtener más información detallada sobre cada tipo de beca en nuestra página web o comunicándote con la oficina de becas y ayudas financieras.",
"Ofrecemos varias opciones de becas, desde becas académicas hasta becas deportivas. Para conocer los requisitos y aplicar, te recomiendo visitar nuestra página de becas o contactar a la oficina correspondiente.",
"Tenemos diferentes opciones de becas, incluyendo becas académicas y de necesidades económicas. Puedes encontrar información detallada sobre cada tipo de beca en nuestra página oficial o contactando a la oficina de becas.",
"Contamos con opciones de becas académicas, deportivas y de mérito. Si estás interesado, te sugiero revisar nuestra página web o ponerte en contacto con la oficina de becas para obtener detalles sobre requisitos y plazos de solicitud.",
"Ofrecemos varias opciones de becas, desde becas académicas hasta becas deportivas. Obtén información detallada sobre cada tipo de beca en nuestra página de becas o comunícate con la oficina correspondiente.",
"Tenemos diferentes opciones de becas, incluyendo becas académicas y de necesidades económicas. Puedes encontrar información detallada sobre cada tipo de beca en nuestra página oficial o contactando a la oficina de becas.",
"Contamos con opciones de becas académicas, deportivas y de mérito. Si estás interesado, te sugiero revisar nuestra página web o ponerte en contacto con la oficina de becas para obtener detalles sobre requisitos y plazos de solicitud.",
"Ofrecemos varias opciones de becas, desde becas académicas hasta becas deportivas. Obtén información detallada sobre cada tipo de beca en nuestra página de becas o comunícate con la oficina correspondiente.",
"Tenemos diferentes opciones de becas, incluyendo becas académicas y de necesidades económicas. Puedes encontrar información detallada sobre cada tipo de beca en nuestra página oficial o contactando a la oficina de becas.",
"Contamos con opciones de becas académicas, deportivas y de mérito. Si estás interesado, te sugiero revisar nuestra página web o ponerte en contacto con la oficina de becas para obtener detalles sobre requisitos y plazos de solicitud.",
"Ofrecemos varias opciones de becas, desde becas académicas hasta becas deportivas. Obtén información detallada sobre cada tipo de beca en nuestra página de becas o comunícate con la oficina correspondiente.",
"Tenemos diferentes opciones de becas, incluyendo becas académicas y de necesidades económicas. Puedes encontrar información detallada sobre cada tipo de beca en nuestra página oficial o contactando a la oficina de becas.",
"Contamos con opciones de becas académicas, deportivas y de mérito. Si estás interesado, te sugiero revisar nuestra página web o ponerte en contacto con la oficina de becas para obtener detalles sobre requisitos y plazos de solicitud.",
"Ofrecemos varias opciones de becas, desde becas académicas hasta becas deportivas. Obtén información detallada sobre cada tipo de beca en nuestra página de becas o comunícate con la oficina correspondiente.",
"Tenemos diferentes opciones de becas, incluyendo becas académicas y de necesidades económicas. Puedes encontrar información detallada sobre cada tipo de beca en nuestra página oficial o contactando a la oficina de becas.",
"Contamos con opciones de becas académicas, deportivas y de mérito. Si estás interesado, te sugiero revisar nuestra página web o ponerte en contacto con la oficina de becas para obtener detalles sobre requisitos y plazos de solicitud. Además, ofrecemos becas específicas para diferentes programas académicos, así que asegúrate de explorar todas las oportunidades disponibles. ¡No dudes en preguntar si necesitas más información!",
"Ofrecemos varias opciones de becas, desde becas académicas hasta becas deportivas. Obtén información detallada sobre cada tipo de beca en nuestra página de becas o comunícate con la oficina correspondiente. Además, si tienes preguntas específicas sobre los criterios de elegibilidad o el proceso de solicitud, estaré encantado de ayudarte a obtener la información que necesitas.",
"Tenemos diferentes opciones de becas, incluyendo becas académicas y de necesidades económicas. Puedes encontrar información detallada sobre cada tipo de beca en nuestra página oficial o contactando a la oficina de becas.",
"¡Hola! Contamos con opciones de becas académicas, deportivas y de mérito. Si estás interesado, te sugiero revisar nuestra página web o ponerte en contacto con la oficina de becas para obtener detalles sobre requisitos y plazos de solicitud. También ofrecemos talleres informativos sobre becas, así que asegúrate de estar atento a los eventos programados para obtener asesoramiento adicional.",
"Saludos. Ofrecemos varias opciones de becas, desde becas académicas hasta becas deportivas. Obtén información detallada sobre cada tipo de beca en nuestra página de becas o comunícate con la oficina correspondiente. Además, si tienes excelencia académica, podrías ser elegible para becas específicas basadas en el rendimiento académico. ¡Estoy aquí para responder cualquier pregunta adicional que puedas tener!"
]

RESPUESTA_CLASES = [
"Los horarios de clases varían según la carrera. Pueden ser matutinos, vespertinos o mixtos. Para detalles específicos, te recomiendo consultar nuestra página de horarios: [enlace].",
"En nuestra universidad, los horarios de clases se adaptan a las necesidades de cada carrera. Ofrecemos opciones matutinas, vespertinas y mixtas.",
"La disponibilidad de horarios de clases depende de la carrera que elijas. Ofrecemos horarios matutinos, vespertinos y mixtos para adaptarnos a tus necesidades académicas.",
"Los horarios de clases son flexibles y varían según la carrera. Tenemos opciones matutinas, vespertinas y mixtas.",
"En nuestra institución, los horarios de clases son personalizables según la carrera. Ofrecemos horarios matutinos, vespertinos y mixtos para adaptarnos a tu agenda. Más información en [enlace].",
"Los horarios de clases son adaptables a la carrera que elijas. Tanto matutinos, vespertinos como mixtos están disponibles. Para detalles específicos, visita nuestra página de horarios: [enlace].",
"En nuestra universidad, entendemos que cada carrera tiene necesidades diferentes. Por eso, ofrecemos horarios matutinos, vespertinos y mixtos.",
"La flexibilidad es clave en nuestros horarios de clases. Ofrecemos horarios matutinos, vespertinos y mixtos según la carrera. Para detalles específicos, visita nuestra página de horarios: [enlace].",
"Los horarios de clases varían según la carrera que elijas. Tendrás opciones matutinas, vespertinas y mixtas para adaptarte a tu estilo de vida. Encuentra más información en [enlace].",
"En nuestra institución, los horarios de clases se ajustan a la diversidad de carreras. Puedes elegir entre horarios matutinos, vespertinos o mixtos.",
"La variedad de carreras se refleja en nuestros horarios de clases. Ofrecemos opciones matutinas, vespertinas y mixtas",
"Los horarios de clases son personalizables y dependen de la carrera. Ofrecemos horarios matutinos, vespertinos y mixtos",
"En nuestra universidad, los horarios de clases se adaptan a las necesidades de cada estudiante. Puedes elegir entre horarios matutinos, vespertinos o mixtos según la carrera.",
"La flexibilidad es clave en nuestros horarios de clases. Ofrecemos opciones matutinas, vespertinas y mixtas para adaptarnos a tu agenda académica.",
"Los horarios de clases varían según la carrera que elijas. Tendrás opciones matutinas, vespertinas y mixtas para adaptarte a tu estilo de vida..",
"En nuestra institución, los horarios de clases se ajustan a la diversidad de carreras. Puedes elegir entre horarios matutinos, vespertinos o mixtos. Para detalles, visita nuestra página de horarios: [enlace].",
"La variedad de carreras se refleja en nuestros horarios de clases. Ofrecemos opciones matutinas, vespertinas y mixtas.",
"Los horarios de clases son personalizables y dependen de la carrera. Ofrecemos horarios matutinos, vespertinos y mixtos.",
"¡Hola, soy Chato!, En nuestra universidad, los horarios de clases se adaptan a las necesidades de cada estudiante. Puedes elegir entre horarios matutinos, vespertinos o mixtos según la carrera. Consulta nuestra página de horarios: [enlace].",
"¡Saludos dice Chato!, La flexibilidad es clave en nuestros horarios de clases. Ofrecemos opciones matutinas, vespertinas y mixtas para adaptarnos a tu agenda académica. Para más detalles, visita [enlace]."
]

RESPUESTA_EXTRACURRICULARES = [
"Participar en actividades extracurriculares es fácil. Puedes unirte a clubes estudiantiles, equipos deportivos o grupos de interés. Consulta la lista de actividades en nuestra página web o visita el centro de estudiantes para obtener más información.",
"Para participar en actividades extracurriculares, explora las opciones disponibles en nuestra página de clubes y organizaciones estudiantiles. Luego, regístrate para unirte a las actividades que más te interesen. ¡Es una excelente manera de enriquecer tu experiencia universitaria!",
"Participar en actividades extracurriculares es una forma emocionante de involucrarte en la vida universitaria. Consulta la variedad de opciones disponibles en nuestra página web y únete a aquellas que coincidan con tus intereses y habilidades.",
"En nuestra universidad, te animamos a participar en actividades extracurriculares. Desde eventos culturales hasta clubes académicos, hay muchas opciones. Explora nuestras actividades en línea o visita la oficina de vida estudiantil para más detalles.",
"Participar en actividades extracurriculares es fácil y divertido. Revisa la lista de clubes y eventos en nuestra página web, elige tus favoritos y únete a ellos. ¡Es una excelente manera de conocer gente nueva y desarrollar habilidades adicionales!",
"Las actividades extracurriculares son una parte integral de la experiencia universitaria. Puedes encontrar información sobre clubes, eventos y oportunidades en nuestra página web. ¡Anímate a explorar y unirte a lo que te apasione!",
"Para participar en actividades extracurriculares, visita nuestra página de clubes y organizaciones estudiantiles. Allí encontrarás una amplia variedad de opciones para unirte a grupos que se alineen con tus intereses. ¡Diviértete y haz nuevas amistades!",
"Participar en actividades extracurriculares es fácil. Explora la lista de clubes y eventos en nuestra página web, elige tus favoritos y únete. También puedes preguntar en la oficina de vida estudiantil para obtener más información.",
"En nuestra universidad fomentamos la participación en actividades extracurriculares. Revisa la lista de clubes y eventos en nuestra página web, y selecciona aquellos que te interesen. ¡Es una excelente manera de enriquecer tu experiencia universitaria!",
"Anímate a participar en actividades extracurriculares explorando los clubes y eventos disponibles en nuestra página web. Regístrate para unirte a los que te interesen y conoce a otros estudiantes con tus mismos intereses.",
"Participar en actividades extracurriculares es sencillo. Consulta la lista de opciones en nuestra página web y únete a los clubes o eventos que más te llamen la atención. ¡Es una excelente manera de conectarte con la comunidad estudiantil!",
"En nuestra universidad valoramos la participación en actividades extracurriculares. Revisa la variedad de opciones en nuestra página web y regístrate para unirte a aquellas que te interesen. ¡Disfruta de una experiencia universitaria completa!",
"Para participar en actividades extracurriculares, visita nuestra página de clubes y organizaciones estudiantiles. Allí encontrarás una amplia variedad de opciones para unirte a grupos que se alineen con tus intereses. ¡Diviértete y haz nuevas amistades!",
"Participar en actividades extracurriculares es fácil. Explora la lista de clubes y eventos en nuestra página web, elige tus favoritos y únete. También puedes preguntar en la oficina de vida estudiantil para obtener más información.",
"En nuestra universidad fomentamos la participación en actividades extracurriculares. Revisa la lista de clubes y eventos en nuestra página web, y selecciona aquellos que te interesen. ¡Es una excelente manera de enriquecer tu experiencia universitaria!",
"Anímate a participar en actividades extracurriculares explorando los clubes y eventos disponibles en nuestra página web. Regístrate para unirte a los que te interesen y conoce a otros estudiantes con tus mismos intereses.",
"Participar en actividades extracurriculares es sencillo. Consulta la lista de opciones en nuestra página web y únete a los clubes o eventos que más te llamen la atención. ¡Es una excelente manera de conectarte con la comunidad estudiantil!",
"En nuestra universidad valoramos la participación en actividades extracurriculares. Revisa la variedad de opciones en nuestra página web y regístrate para unirte a aquellas que te interesen. ¡Disfruta de una experiencia universitaria completa!",
"¡Hola! Para participar en actividades extracurriculares, visita nuestra página de clubes y organizaciones estudiantiles. Allí encontrarás una amplia variedad de opciones para unirte a grupos que se alineen con tus intereses. ¡Diviértete y haz nuevas amistades!",
"Saludos. Participar en actividades extracurriculares es fácil. Explora la lista de clubes y eventos en nuestra página web, elige tus favoritos y únete. También puedes preguntar en la oficina"
]

RESPUESTA_EXAMENES = [
"Sí, en nuestra universidad se realizan exámenes ordinarios para evaluar el progreso académico de los estudiantes.",
"Sí, contamos con exámenes ordinarios como parte del proceso de evaluación regular.",
"Absolutamente, los exámenes ordinarios son una parte esencial de nuestro sistema de evaluación académica.",
"Sí, los exámenes ordinarios son una práctica común en nuestra institución para evaluar el desempeño de los estudiantes.",
"Sí, en nuestros programas académicos se llevan a cabo exámenes ordinarios de forma regular.",
"Sí, parte de nuestra metodología académica incluye la realización de exámenes ordinarios para evaluar el conocimiento adquirido.",
"Sí, los exámenes ordinarios son una parte importante de nuestra estructura de evaluación académica.",
"Sí, en nuestra universidad se programan exámenes ordinarios como parte del calendario académico.",
"Sí, los exámenes ordinarios son una práctica estándar para evaluar el rendimiento académico de los estudiantes.",
"Así es, los exámenes ordinarios son una parte integral de nuestro sistema educativo.",
"Sí, en nuestra institución se realizan exámenes ordinarios para evaluar el progreso de los estudiantes en sus asignaturas.",
"Sí, contamos con exámenes ordinarios que forman parte de la evaluación continua de los estudiantes.",
"Sí, parte de nuestra metodología educativa implica la administración de exámenes ordinarios en ciertos periodos del año.",
"Sí, en nuestra universidad se llevan a cabo exámenes ordinarios como parte de la rutina académica.",
"Sí, contamos con exámenes ordinarios que permiten medir el nivel de conocimiento adquirido por los estudiantes.",
"Sí, los exámenes ordinarios son una herramienta fundamental para evaluar el rendimiento académico de nuestros estudiantes.",
"Sí, en nuestra institución se programan exámenes ordinarios de manera regular durante el año académico.",
"Sí, los exámenes ordinarios son una práctica establecida en nuestra universidad para evaluar el desempeño estudiantil.",
"¡Hola, soy Chato! hoSí, realizamos exámenes ordinarios como parte de nuestro enfoque en la evaluación continua.",
"¡Saludos! Así es, en nuestra universidad se programan exámenes ordinarios como parte del proceso de evaluación académica."
]


def get_response(user_input):
     split_message = re.split(r'\s|[,:;.?!-_]\s*',user_input.lower())
     response = check_all_messages(split_message)
     return response

def message_probability(user_message,recognized_words,required_word=[]):
     message_certainty = 0
     if(len(required_word)) == 0:
          has_required_words = True
     else:
          has_required_words = False
     for word in user_message:
          if word in recognized_words:
               message_certainty += 1
     percentage = float(message_certainty) / float (len(recognized_words))
     for word in required_word:
          if word in user_message:
               has_required_words = True
     if has_required_words:
          return int(percentage*100)
     else:
          return 0
     
def check_all_messages(message):
     global saludo
     activar_hola = False
     highest_prob = {}
     def response(bot_response,list_of_words, required_word = []):
          global saludo
          nonlocal highest_prob
          nonlocal activar_hola
          if bot_response == RESPUESTA_HOLA or bot_response == RESPUESTA_ADIOS:
               highest_prob[bot_response[random.randrange(0,19)]] = message_probability(message,list_of_words,required_word)
          elif saludo:
               highest_prob[bot_response[random.randrange(0,17)]] = message_probability(message,list_of_words,required_word)
          else:
               highest_prob[bot_response[random.randrange(18,19)]] = message_probability(message,list_of_words,required_word)
               activar_hola = True

     response(RESPUESTA_HOLA,['hola','buenas','saludos','ayuda','tardes','dias','noches','onda'])
     response(RESPUESTA_PROCESO,['proceso','admisión','admision','informes','necesito','universidad','cuando'],required_word=['proceso','adimision','admisión'])
     response(RESPUESTA_CARRERAS,['carreras','carrera','imparten','ofrecen','áreas','universidad','que'],required_word=['carreras','imparten','ofrecen'])
     response(RESPUESTA_REQUISITOS,['requisitos','papeles','admision','requerimientos','documentos','entrar','universidad','cuales'],required_word=['requisitos','papeles','requerimientos'])
     response(RESPUESTA_ADIOS,['adios','luego','bye','despido','voy','me','hasta','gracias'])
     response(RESPUESTA_INTERCAMBIOS,['programas','intercambio','intercambios','estudiantil','ofrecen','intercambio','cuales'],required_word=['intercambio','programas','estudiantil'])
     response(RESPUESTA_BECAS,['becas','ofrecen','opciones','beca','disponibles','que'],required_word=['becas','opciones'])
     response(RESPUESTA_CLASES,['horarios','clases','horario','turno','cuales'],required_word=['clases','horarios','turno'])
     response(RESPUESTA_EXTRACURRICULARES,['actividades','extracurriculares','participar','participacion','como','puedo','actividad','extracurricular'],required_word=['actividades','extracurriculares'])
     response(RESPUESTA_EXAMENES,['examenes','ordinarios','hay'],required_word=['examenes'])
     best_match = max(highest_prob, key=highest_prob.get)
     if best_match in RESPUESTA_HOLA or activar_hola:
          saludo = True
     if best_match in RESPUESTA_ADIOS:
          saludo = False
     return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
     return ["¿Puedes decirlo de nuevo?",
     "No estoy seguro de lo que quieres",
     "Búscalo en Google a ver que tal",
     "No entendí lo que escribiste, ¿podrías ser más específico?",
     "Lo siento, estoy teniendo dificultades para comprender, ¿puedes reformular tu pregunta?",
     "Tu solicitud no está clara para mí en este momento, ¿puedes proporcionar más detalles?",
     "Parece que hay un malentendido, ¿puedes explicar tu pregunta de otra manera?",
     "Estoy teniendo problemas para interpretar tu mensaje, ¿puedes expresarlo de otra manera?",
     "Lo siento, no estoy seguro de entender completamente. ¿Podrías proporcionar más información?",
     "Tengo problemas para captar la idea. ¿Podrías explicarlo de otra manera?"][random.randrange(10)]

saludo = False
while(True):
     print("Bot:" + get_response(input("You:" )))
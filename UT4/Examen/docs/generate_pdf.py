import os
import base64
import subprocess

PROJECT_DIR = "/home/antonio/Documentos/DAM/Acceso-a-Datos/UT4/Examen"
CAPTURES_DIR = os.path.join(PROJECT_DIR, "docs/capturas")
OUTPUT_PDF = os.path.join(PROJECT_DIR, "Documentacion_UT4_Antonio_Cano_Ruiz.pdf")
TMP_HTML = os.path.join(PROJECT_DIR, "docs/documentacion_print.html")

def get_base64_img(filename):
    path = os.path.join(CAPTURES_DIR, filename)
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/png;base64,{data}"

img1 = get_base64_img("01_script_sql_postgresql.png")
img2 = get_base64_img("02_datos_insertados_psql.png")
img3 = get_base64_img("03_estructura_proyecto_pom.png")
img4 = get_base64_img("04_configuracion_hibernate.png")
img5 = get_base64_img("05_entidad_planeta.png")
img6 = get_base64_img("06_jerarquia_nave_abstracta.png")
img7 = get_base64_img("07_subclases_polimorficas.png")
img8 = get_base64_img("08_desafio1_hql_type.png")
img9 = get_base64_img("09_desafio2_hql_fetch_join.png")
img10 = get_base64_img("10_desafio3_hql_proyeccion.png")
img11 = get_base64_img("11_ejecucion_main_resultados.png")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Documentación UT4 - Persistencia - Antonio Cano Ruiz</title>
<style>
  @page {{
    size: A4;
    margin: 18mm 15mm 20mm 15mm;
    @bottom-right {{
      content: counter(page);
    }}
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1e293b;
    line-height: 1.6;
    font-size: 11pt;
    background: #ffffff;
  }}

  /* PORTADA */
  .cover-page {{
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    padding: 40px 20px 20px 20px;
  }}

  .cover-header {{
    border-bottom: 4px solid #2563eb;
    padding-bottom: 25px;
  }}

  .badge {{
    display: inline-block;
    background: #dbeafe;
    color: #1e40af;
    font-weight: 700;
    font-size: 10pt;
    padding: 4px 12px;
    border-radius: 9999px;
    margin-bottom: 15px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .cover-title {{
    font-size: 26pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.2;
    margin-bottom: 12px;
  }}

  .cover-subtitle {{
    font-size: 14pt;
    color: #475569;
    font-weight: 400;
    line-height: 1.4;
  }}

  .cover-body {{
    margin: 40px 0;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 6px solid #2563eb;
    border-radius: 8px;
    padding: 24px;
  }}

  .cover-body h3 {{
    font-size: 13pt;
    color: #0f172a;
    margin-bottom: 12px;
  }}

  .cover-body ul {{
    list-style-type: none;
    padding-left: 0;
  }}

  .cover-body li {{
    margin-bottom: 8px;
    font-size: 11pt;
    color: #334155;
  }}

  .cover-body li strong {{
    color: #0f172a;
  }}

  .cover-footer {{
    background: #0f172a;
    color: #f8fafc;
    border-radius: 8px;
    padding: 24px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }}

  .footer-col p {{
    margin: 4px 0;
    font-size: 10.5pt;
  }}

  .footer-label {{
    color: #94a3b8;
    font-size: 9pt;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .footer-val {{
    font-weight: 600;
    color: #ffffff;
  }}

  /* CONTENIDO GENERAL */
  .page-break {{
    page-break-before: always;
  }}

  h1 {{
    font-size: 18pt;
    color: #0f172a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 8px;
    margin-top: 24px;
    margin-bottom: 14px;
  }}

  h2 {{
    font-size: 14pt;
    color: #1e3a8a;
    margin-top: 20px;
    margin-bottom: 10px;
  }}

  h3 {{
    font-size: 12pt;
    color: #0f172a;
    margin-top: 14px;
    margin-bottom: 6px;
  }}

  p {{
    margin-bottom: 12px;
    text-align: justify;
  }}

  ul, ol {{
    margin-left: 24px;
    margin-bottom: 14px;
  }}

  li {{
    margin-bottom: 6px;
  }}

  strong {{
    color: #0f172a;
  }}

  /* CAJAS DE NOTA */
  .callout {{
    background: #eff6ff;
    border-left: 4px solid #3b82f6;
    padding: 12px 16px;
    margin: 14px 0;
    border-radius: 4px;
    font-size: 10.5pt;
  }}

  .callout-title {{
    font-weight: 700;
    color: #1d4ed8;
    margin-bottom: 4px;
  }}

  .callout-warning {{
    background: #fffbeb;
    border-left-color: #f59e0b;
  }}
  .callout-warning .callout-title {{
    color: #b45309;
  }}

  .callout-success {{
    background: #f0fdf4;
    border-left-color: #22c55e;
  }}
  .callout-success .callout-title {{
    color: #15803d;
  }}

  /* CÓDIGO */
  code {{
    font-family: "JetBrains Mono", Consolas, "Courier New", monospace;
    font-size: 9.5pt;
    background: #f1f5f9;
    padding: 2px 6px;
    border-radius: 4px;
    color: #0f172a;
    border: 1px solid #e2e8f0;
  }}

  pre {{
    background: #0f172a;
    color: #e2e8f0;
    padding: 12px 16px;
    border-radius: 6px;
    font-family: "JetBrains Mono", Consolas, monospace;
    font-size: 9pt;
    line-height: 1.45;
    margin: 12px 0;
    overflow-x: auto;
  }}

  /* IMÁGENES / FIGURAS */
  .figure-box {{
    margin: 18px 0;
    text-align: center;
    page-break-inside: avoid;
  }}

  .figure-box img {{
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    border: 1px solid #cbd5e1;
  }}

  .figure-caption {{
    margin-top: 8px;
    font-size: 9.5pt;
    color: #64748b;
    font-style: italic;
  }}

  /* TABLAS */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 10pt;
  }}

  th, td {{
    border: 1px solid #cbd5e1;
    padding: 8px 12px;
    text-align: left;
  }}

  th {{
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 600;
  }}

  tr:nth-child(even) {{
    background: #f8fafc;
  }}
</style>
</head>
<body>

<!-- PORTADA -->
<div class="cover-page">
  <div class="cover-header">
    <div class="badge">Práctica de Examen Práctico Evaluativo</div>
    <div class="cover-title">Sistema de Inteligencia Táctica HoloNet</div>
    <div class="cover-subtitle">Herramientas de Mapeo Objeto-Relacional (Hibernate 6 / JPA)<br>Estrategia Jerárquica de Persistencia: Tabla Única (SINGLE_TABLE)</div>
  </div>

  <div class="cover-body">
    <h3>Resumen Técnico del Proyecto</h3>
    <p>Construcción de una arquitectura de persistencia polimórfica en Java con Hibernate 6 y PostgreSQL para resolver el desfase objeto-relacional (<em>Impedance Mismatch</em>). Se implementa un modelo jerárquico unificado, asociaciones perezosas y consultas de alto rendimiento en HQL avanzado para el control táctico de la flota.</p>
    <ul>
      <li>✔ <strong>Persistencia Polimórfica:</strong> Estrategia <code>InheritanceType.SINGLE_TABLE</code> con discriminador dinámico.</li>
      <li>✔ <strong>Optimización de Consultas:</strong> Mitigación del problema N+1 mediante <code>INNER JOIN FETCH</code>.</li>
      <li>✔ <strong>Filtrado Polimórfico en ORM:</strong> Uso de la función <code>TYPE(n)</code> y proyecciones tabulares escalares.</li>
      <li>✔ <strong>Control Transaccional Seguro:</strong> Gestión de sesiones mediante el patrón <em>try-with-resources</em>.</li>
    </ul>
  </div>

  <div class="cover-footer">
    <div class="footer-col">
      <div class="footer-label">Alumno / Desarrollador</div>
      <div class="footer-val">Antonio Cano Ruiz</div>
      <div style="margin-top: 8px;" class="footer-label">Ciclo Formativo</div>
      <div class="footer-val">2º Desarrollo de Aplicaciones Multiplataforma (DAM)</div>
    </div>
    <div class="footer-col">
      <div class="footer-label">Módulo Profesional</div>
      <div class="footer-val">Acceso a Datos (Código: 2627)</div>
      <div style="margin-top: 8px;" class="footer-label">Unidad de Trabajo</div>
      <div class="footer-val">UT4 - Persistencia (Hibernate 6 / JPA)</div>
    </div>
  </div>
</div>

<!-- SECCIÓN 1: INTRODUCCIÓN -->
<div>
  <h1>1. Introducción y Planteamiento del Problema</h1>
  <p>En el desarrollo de software empresarial contemporáneo, uno de los desafíos más críticos es el <strong>desfase objeto-relacional (<em>Object-Relational Impedance Mismatch</em>)</strong>. Este fenómeno surge al intentar conciliar el paradigma orientado a objetos (que maneja herencia, polimorfismo, encapsulamiento e identidad) con el modelo relacional tradicional (basado en tablas planas, relaciones de claves foráneas y álgebra relacional).</p>

  <p>El proyecto <strong>HoloNet</strong> aborda este problema para el departamento de inteligencia militar, que requiere clasificar y controlar el censo de activos navales interceptados en el Borde Exterior (cazas ligeros y destructores estelares) asignados a distintos sistemas planetarios.</p>

  <div class="callout callout-success">
    <div class="callout-title">Objetivos de la Práctica</div>
    <ul>
      <li>Mapear una jerarquía de clases POO en una única tabla física (<code>InheritanceType.SINGLE_TABLE</code>).</li>
      <li>Implementar asociaciones <code>@ManyToOne</code> con carga perezosa controlada (<code>FetchType.LAZY</code>).</li>
      <li>Resolver retos tácticos mediante consultas avanzadas en HQL evitando consultas SQL nativas.</li>
      <li>Demostrar la mitigación empírica del problema de rendimiento N+1.</li>
    </ul>
  </div>
</div>

<!-- SECCIÓN 2: BASE DE DATOS POSTGRESQL -->
<div class="page-break">
  <h1>2. Fase 1: Infraestructura de Datos Desnormalizada (PostgreSQL)</h1>
  <p>Para implementar la estrategia de <strong>Tabla Única</strong>, toda la jerarquía de naves de la aplicación Java debe persistirse físicamente en una única tabla relacional denominada <code>naves</code>, complementada por la tabla <code>planetas</code> que modela las bases de despliegue.</p>

  <h2>2.1. Diseño del Esquema Relacional (DDL)</h2>
  <p>Esta tabla física cuenta con las siguientes particularidades obligatorias de la estrategia de tabla única:</p>
  <ul>
    <li><strong>Columna Discriminadora (<code>tipo_nave</code>):</strong> Columna de tipo <code>VARCHAR(30)</code> no nula que almacena el identificador del subtipo (<code>'CAZA'</code> o <code>'DESTRUCTOR'</code>) para que el motor Hibernate instancie la subclase correcta en tiempo de ejecución.</li>
    <li><strong>Atributos Específicos Nulables:</strong> Las columnas <code>potencia_fuego</code> (propia de los cazas) y <code>capacidad_escudos</code> (propia de los destructores) deben permitir valores <code>NULL</code>, dado que ninguna fila utilizará ambas columnas simultáneamente.</li>
    <li><strong>Integridad Referencial:</strong> Clave foránea <code>fk_planeta</code> con comportamiento <code>ON DELETE SET NULL</code> para garantizar que la destrucción de una base no elimine el registro histórico de la nave.</li>
  </ul>

  <div class="figure-box">
    <img src="{img1}" alt="Script DDL PostgreSQL">
    <div class="figure-caption">Figura 1: Creación de tablas en PostgreSQL con columna discriminadora y atributos desnormalizados.</div>
  </div>

  <h2>2.2. Verificación de Datos Semilla</h2>
  <p>Se introdujeron los planetas (Coruscant, Yavin IV y Tatooine) con diferentes afiliaciones políticas, así como 5 naves de prueba combinando tipos y estados del sistema (<code>Estable</code>, <code>Critico</code> y <code>Mantenimiento</code>):</p>

  <div class="figure-box">
    <img src="{img2}" alt="Datos Semilla en PostgreSQL">
    <div class="figure-caption">Figura 2: Consulta tabular de verificación en PostgreSQL con las 5 naves y 3 planetas insertados.</div>
  </div>
</div>

<!-- SECCIÓN 3: ARQUITECTURA DEL PROYECTO -->
<div class="page-break">
  <h1>3. Fase 2: Configuración del Motor ORM y Estructura</h1>

  <h2>3.1. Gestión de Dependencias (Maven)</h2>
  <p>El proyecto utiliza Apache Maven para orquestar la compilación y gestionar las bibliotecas esenciales: Hibernate ORM Core 6.4.4 (especificación Jakarta Persistence) y el controlador JDBC oficial de PostgreSQL 42.7.2.</p>

  <div class="figure-box">
    <img src="{img3}" alt="Dependencias pom.xml">
    <div class="figure-caption">Figura 3: Dependencias del proyecto en el archivo pom.xml (Hibernate 6.4.4.Final y PostgreSQL Driver).</div>
  </div>

  <h2>3.2. Descriptor Central de Hibernate (<code>hibernate.cfg.xml</code>)</h2>
  <p>El archivo de configuración establece las credenciales a la base de datos <code>hangar_imperio_db</code>, el dialecto optimizado para PostgreSQL y los parámetros de auditoría <code>show_sql</code> y <code>format_sql</code> para inspeccionar el SQL generado por detrás.</p>

  <div class="figure-box">
    <img src="{img4}" alt="Configuración hibernate.cfg.xml">
    <div class="figure-caption">Figura 4: Configuración de SessionFactory y mapeo explícito de entidades en hibernate.cfg.xml.</div>
  </div>

  <h2>3.3. Ciclo de Vida y Sesiones: <code>HibernateUtil.java</code></h2>
  <p>La construcción de una <code>SessionFactory</code> es un proceso pesado en recursos que compila los metadatos y valida los esquemas. Por ello, se implementó el patrón <strong>Singleton</strong> a través de <code>HibernateUtil</code>, asegurando una única instancia durante la vida útil del proceso y permitiendo la invocación controlada de <code>shutdown()</code>.</p>
</div>

<!-- SECCIÓN 4: MODELO DE CLASES -->
<div class="page-break">
  <h1>4. Fase 3: Mapeo de Entidades y Jerarquía Polimórfica (POO / JPA)</h1>

  <h2>4.1. Entidad Básica: <code>Planeta.java</code></h2>
  <p>Mapea la tabla <code>planetas</code> mediante las anotaciones estándar de JPA: <code>@Entity</code>, <code>@Table(name="planetas")</code>, clave primaria con <code>@Id</code> y <code>@GeneratedValue(strategy = GenerationType.IDENTITY)</code>.</p>

  <div class="figure-box">
    <img src="{img5}" alt="Entidad Planeta.java">
    <div class="figure-caption">Figura 5: Mapeo de la entidad Planeta.java con restricciones de unicidad y no nulabilidad.</div>
  </div>

  <h2>4.2. Raíz Jerárquica Abstracta: <code>Nave.java</code></h2>
  <p>La clase abstracta <code>Nave</code> centraliza los atributos comunes (<code>nombre</code>, <code>modelo</code>, <code>estadoSistema</code>) y define la estrategia de herencia para el proveedor de persistencia:</p>
  <ul>
    <li><code>@Inheritance(strategy = InheritanceType.SINGLE_TABLE)</code>: Define que todas las subclases compartirán la tabla <code>naves</code>.</li>
    <li><code>@DiscriminatorColumn(name = "tipo_nave", discriminatorType = DiscriminatorType.STRING)</code>: Especifica el campo de distinción.</li>
    <li><code>@ManyToOne(fetch = FetchType.LAZY)</code>: Configura la relación perezosa hacia <code>Planeta</code> a través de la columna <code>planeta_origen_id</code>. La carga perezosa evita traer datos del planeta hasta que sean explícitamente requeridos.</li>
  </ul>

  <div class="figure-box">
    <img src="{img6}" alt="Clase abstracta Nave.java">
    <div class="figure-caption">Figura 6: Mapeo polimórfico de la clase base abstracta Nave.java con estrategia SINGLE_TABLE y carga LAZY.</div>
  </div>

  <h2>4.3. Subclases Especializadas: <code>CazaLigero</code> y <code>DestructorEstelar</code></h2>
  <p>Cada subclase extiende a <code>Nave</code> e implementa su respectivo <code>@DiscriminatorValue</code> junto con sus propiedades específicas:</p>

  <div class="figure-box">
    <img src="{img7}" alt="Subclases CazaLigero y DestructorEstelar">
    <div class="figure-caption">Figura 7: Mapeo de las subclases CazaLigero (CAZA) y DestructorEstelar (DESTRUCTOR).</div>
  </div>
</div>

<!-- SECCIÓN 5: DESAFÍOS HQL -->
<div class="page-break">
  <h1>5. Fase 4: Desafíos de Inteligencia Táctica (HQL Avanzado)</h1>
  <p>Todas las consultas se desarrollaron en la clase de servicio <code>HoloNetService</code>, empleando sesiones seguras con <em>try-with-resources</em> y parámetros con nombre (evitando inyecciones HQL).</p>

  <h2>5.1. Desafío 1: Sensor de Escuadrones Polimórfico (INNER JOIN + TYPE)</h2>
  <p><strong>Firma:</strong> <code>public List&lt;CazaLigero&gt; obtenerCazasOperativosPorBando(String bando)</code></p>
  <p><strong>Requisitos y Solución:</strong> Recupera únicamente cazas operativos de un bando. La consulta une la nave con su propiedad <code>planetaOrigen</code> mediante <code>INNER JOIN</code> y filtra por <code>TYPE(n) = CazaLigero</code>, descartando los cazas en estado <code>'Mantenimiento'</code>.</p>

  <div class="figure-box">
    <img src="{img8}" alt="Desafío 1 HQL">
    <div class="figure-caption">Figura 8: Implementación del Desafío 1 con discriminador polimórfico TYPE(n) e INNER JOIN en HQL.</div>
  </div>

  <h2>5.2. Desafío 2: Mitigación de Consultas Recurrentes (FETCH JOIN)</h2>
  <p><strong>Firma:</strong> <code>public List&lt;Nave&gt; obtenerFlotaCriticaPolimorfica()</code></p>
  <p><strong>Requisitos y Solución:</strong> Recupera naves de cualquier tipo en estado <code>'Critico'</code>. Al estar configurada la relación como <code>FetchType.LAZY</code>, un acceso convencional causaría el <strong>problema N+1</strong> (1 consulta para la lista y $N$ consultas secundarias para el planeta de cada nave). Se mitiga aplicando <code>INNER JOIN FETCH n.planetaOrigen p</code>, forzando la hidratación inmediata en una sola sentencia SQL.</p>

  <div class="figure-box">
    <img src="{img9}" alt="Desafío 2 HQL FETCH JOIN">
    <div class="figure-caption">Figura 9: Desafío 2 con INNER JOIN FETCH eliminando el cuello de botella N+1.</div>
  </div>

  <h2>5.3. Desafío 3: Proyecciones Planas de Inteligencia (LEFT JOIN)</h2>
  <p><strong>Firma:</strong> <code>public List&lt;Object[]&gt; obtenerReporteGeneralFiltrado()</code></p>
  <p><strong>Requisitos y Solución:</strong> Extrae un reporte escalar plano proyectando solo tres campos: nombre de la nave, clase concreta en el modelo POO (<code>TYPE(n)</code>) y nombre del planeta. El uso de <code>LEFT JOIN</code> asegura que las naves sin planeta asignado se incluyan con valor <code>null</code>.</p>

  <div class="figure-box">
    <img src="{img10}" alt="Desafío 3 HQL Proyección">
    <div class="figure-caption">Figura 10: Desafío 3 con proyección escalar tabular (List&lt;Object[]&gt;) y LEFT JOIN.</div>
  </div>
</div>

<!-- SECCIÓN 6: RESULTADOS Y CONCLUSIONES -->
<div class="page-break">
  <h1>6. Fase 5: Validación Experimental y Resultados en Consola</h1>
  <p>La clase de prueba <code>MainHangar</code> inicializa el contexto de Hibernate y ejecuta los tres desafíos de forma secuencial, permitiendo contrastar la salida en consola con las sentencias SQL reales generadas:</p>

  <div class="figure-box">
    <img src="{img11}" alt="Salida de consola de MainHangar">
    <div class="figure-caption">Figura 11: Ejecución completa en consola verificando la corrección funcional de los tres desafíos.</div>
  </div>

  <h2>6.1. Análisis Detallado de Resultados</h2>
  <table>
    <thead>
      <tr>
        <th>Desafío</th>
        <th>Entrada / Bando</th>
        <th>Resultado Obtenido</th>
        <th>Verificación Técnica</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3"><strong>1. Cazas Operativos</strong></td>
        <td>Neutral</td>
        <td>0 naves</td>
        <td>Halcón Milenario en Tatooine descartado por estado 'Mantenimiento'.</td>
      </tr>
      <tr>
        <td>Imperio</td>
        <td>1 nave (Caza TIE Alfa)</td>
        <td>En Coruscant, estado 'Critico' &ne; 'Mantenimiento'. Potencia: 40.</td>
      </tr>
      <tr>
        <td>Alianza Rebelde</td>
        <td>1 nave (Caza X-Wing)</td>
        <td>En Yavin IV, estado 'Estable'. Potencia: 85.</td>
      </tr>
      <tr>
        <td><strong>2. Flota Crítica</strong></td>
        <td>Estado 'Critico'</td>
        <td>Superdestructor Ejecutor (45000 escudos) y Caza TIE Alfa (40 potencia)</td>
        <td>Carga polimórfica instantánea del planeta con 1 sola consulta SQL (Fetch Join).</td>
      </tr>
      <tr>
        <td><strong>3. Reporte General</strong></td>
        <td>Toda la flota</td>
        <td>5 registros proyectados con clase Java y planeta origen</td>
        <td>Proyección escalar optimizada de bajo impacto en memoria mediante Left Join.</td>
      </tr>
    </tbody>
  </table>

  <h1>7. Conclusiones Finales</h1>
  <ol>
    <li><strong>Rendimiento de SINGLE_TABLE:</strong> Es la estrategia más veloz para lectura y operaciones polimórficas masivas, pues delega la distinción al motor mediante una simple columna discriminadora sin realizar <code>UNION</code> ni múltiples <code>JOIN</code> entre tablas secundarias.</li>
    <li><strong>Poder Expresivo de HQL:</strong> Permite consultar el modelo de objetos directamente respetando la herencia y polimorfismo mediante constructos como <code>TYPE(n)</code>.</li>
    <li><strong>Control del Problema N+1:</strong> La combinación de <code>FetchType.LAZY</code> por defecto con <code>FETCH JOIN</code> bajo demanda ofrece el equilibrio óptimo entre ligereza en reposo y eficiencia en consultas críticas.</li>
  </ol>
</div>

</body>
</html>
"""

with open(TMP_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generado en {TMP_HTML}. Procediendo a compilar PDF con Google Chrome...")

cmd = [
    "google-chrome",
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    "--run-all-compositor-stages-before-draw",
    "--print-to-pdf-no-header",
    f"--print-to-pdf={OUTPUT_PDF}",
    f"file://{TMP_HTML}"
]
subprocess.run(cmd, check=True)
print(f"✔ PDF generado exitosamente en: {OUTPUT_PDF}")

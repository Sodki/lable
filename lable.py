import jinja2
import barcode


cliente = {
    "cliente": "alpha",
    "morada": "beta gama delta 4",
    "xpto": 1983413764,
}

template = """
    <html>
      <body>
        <div style="width: 15cm; height: 15cm; border: 1px solid black;">
          <h1>ACME Ltd.</h1>
          <p>
            <b>Cliente:</b> {{cliente}}
          </p>
          <p>
            <b>Morada:</b> {{morada}}
          </p>
          <p>
            <b>Número XPTO:</b> {{xpto}}
          </p>
          <svg width=100 height=100>
            {{xpto | codigo_barras}}
          </svg>
        </div>
      </body>
    <html>
"""


def codigo_barras(codigo):
    return barcode.Gs1_128(
        code=str(codigo),
        writer=barcode.writer.SVGWriter(),
    ).render()


env = jinja2.Environment()
env.filters["codigo_barras"] = codigo_barras
template = env.from_string(template)

print(template.render(cliente))

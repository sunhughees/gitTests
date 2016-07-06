from bs4 import BeautifulSoup
from sys import argv

# how to example
# python generateIconJs.py icon.svg

js_name = argv[1][:-4]

with open(argv[1], "r") as f:
	svg_xml = f.read()

soup_svg_xml = BeautifulSoup(svg_xml)

js_boilerplate = """
let React = require('react');
let IconBase = require('react-icon-base');

export default class %s extends React.Component {
    render() {
        return (
            <IconBase viewBox="0 0 40 40" {...this.props}>
                <g><path d="%s"/></g>
            </IconBase>
        );
    }
}
""" %(js_name, soup_svg_xml.path["d"])

with open(js_name, "w") as f:
	f.write(js_boilerplate)



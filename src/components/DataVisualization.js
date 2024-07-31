import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const DataVisualization = ({ data }) => {
    const svgRef = useRef();

    useEffect(() => {
        const svg = d3.select(svgRef.current);
        // Clear previous SVG content
        svg.selectAll('*').remove();
        // Your D3 visualization code here
    }, [data]);

    return <svg ref={svgRef}></svg>;
};

export default DataVisualization;

import unittest
from unittest.mock import MagicMock
import matplotlib.pyplot as plt

import conversationalspacemapapp.Parser.TranscriptParser as TranscriptParser
import conversationalspacemapapp.Plotter.PlotMap as PlotMap


class TestPlotMap(unittest.TestCase):
    parser: TranscriptParser.AbstractParser
    fig: plt.figure()
    ax: plt.Axes

    def setUp(self):
        TestPlotMap.parser = MagicMock()
        TestPlotMap.parser.map_list = [-10, 15, -5]
        TestPlotMap.fig, TestPlotMap.ax = plt.subplots()

    def tearDown(self):
        TestPlotMap.fig.show()

    def test_bar_plot(self):
        plotter = PlotMap.MapBarPlot(
            parser=TestPlotMap.parser,
            ax=TestPlotMap.ax,
            fig=TestPlotMap.fig
        )
        self.assertEqual(
            TestPlotMap.parser.map_list,
            [-10, 15, -5]
        )
        plotter.plot("I01")
        

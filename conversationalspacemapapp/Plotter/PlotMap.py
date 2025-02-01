import matplotlib.pyplot as plt

import conversationalspacemapapp.App.AbstractApp as AbstractApp
import conversationalspacemapapp.Parser.TimestampParser as TranscriptParser


class MapBarPlot:
    def __init__(
        self,
        parser: TranscriptParser.AbstractParser,
        fig: plt.figure,
        app: AbstractApp.AbstractApp,
    ):
        self.participants = parser.participants
        self.map = parser.map
        self.fig = fig
        self.ax = self.fig.gca()
        self.app = app

    def plot(
        self,
        title="Conversational Map Space",
        show_title=True,
        labels=True,
        interviewer_label="Interviewer",
        interviewee_label="Interviewee",
        yaxis=True,
        xaxis=True,
        grid=True,
        legend=True,
    ):
        xlim_num = 0
        for utterance in self.map:
            self.ax.barh(
                utterance.number,
                utterance.words
                * self.app._get_participant_role(utterance.speaker).constant,
                align="center",
                height=0.8,
                color=self.app._get_participant_color(utterance.speaker),
                label=self.app._get_participant_name(utterance.speaker),
            )
            xlim_num = max([abs(utterance.words) for utterance in self.map]) * 1.1
        index = [*range(1, len(self.map) + 1)]

        # Set x-axis
        self.ax.set_xlim([-xlim_num, xlim_num])
        if not xaxis:
            self.ax.set(xticklabels=[])
            self.ax.tick_params(bottom=False)

        # Set grid
        if grid:
            self.ax.xaxis.grid(
                True, linestyle="--", which="major", color="grey", alpha=0.25
            )

        # Set y-axis
        self.ax.set_ylim([-2, max(index) + 2])
        if yaxis:
            self.ax.set_yticks(index)
            self.ax.set_ylabel("Utterance (bottom = start of interview)")
        else:
            self.ax.set(yticklabels=[])
            self.ax.tick_params(left=False)

        # Set plot labels
        if show_title:
            self.ax.set_title(title)
        if labels:
            self.ax.text(
                xlim_num / 2,
                -1,
                interviewee_label + "'s words per utterance",
                horizontalalignment="center",
            )
            self.ax.text(
                -xlim_num / 2,
                -1,
                interviewer_label + "'s words per utterance",
                horizontalalignment="center",
            )
        if legend:
            self.ax.legend(loc="upper left")
            self.remove_duplicate_labels_legend()

    def remove_duplicate_labels_legend(self):
        handles, labels = self.ax.get_legend_handles_labels()
        unique = [
            (h, l)
            for i, (h, l) in enumerate(zip(handles, labels))
            if l not in labels[:i]
        ]
        self.ax.legend(*zip(*unique))

    def save(self, filename: str):
        self.fig.savefig(filename, dpi=300)

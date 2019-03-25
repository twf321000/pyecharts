# coding=utf-8
from ..commons.types import List, Numeric, Optional, Sequence, Union
from ..globals import RenderType
from ..options.series_options import (
    LabelOpts,
    LineStyleOpts,
    SplitLineOpts,
    TextStyleOpts,
)


class InitOpts:
    def __init__(
        self,
        width: str = "900px",
        height: str = "500px",
        chart_id: Optional[str] = None,
        renderer: str = RenderType.CANVAS,
        page_title: str = "Awesome-pyecharts",
        theme: str = "white",
        bg_color: Optional[str] = None,
        js_host: str = "",
    ):
        self.width = width
        self.height = height
        self.chart_id = chart_id
        self.renderer = renderer
        self.page_title = page_title
        self.theme = theme
        self.bg_color = bg_color
        self.js_host = js_host


class ToolBoxFeatureOpts:
    def __init__(
        self,
        save_as_image: Optional[dict] = None,
        restore: Optional[dict] = None,
        data_view: Optional[dict] = None,
        data_zoom: Optional[dict] = None,
    ):
        if not save_as_image:
            save_as_image = {"show": True, "title": "save as image"}
        if not restore:
            restore = {"show": True, "title": "restore"}
        if not data_view:
            data_view = {"show": True, "title": "data view"}
        if not data_zoom:
            data_zoom = {"show": True, "title": "data zoom"}

        self.opts: dict = {
            "saveAsImage": save_as_image,
            "restore": restore,
            "dataView": data_view,
            "dataZoom": data_zoom,
        }


class ToolboxOpts:
    def __init__(
        self,
        is_show: bool = True,
        orient: str = "horizontal",
        pos_left: str = "80%",
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        feature: Union[ToolBoxFeatureOpts, dict] = ToolBoxFeatureOpts(),
    ):
        if isinstance(feature, ToolBoxFeatureOpts):
            feature = feature.opts

        self.opts: dict = {
            "show": is_show,
            "orient": orient,
            "left": pos_left,
            "right": pos_right,
            "top": pos_top,
            "bottom": pos_bottom,
            "feature": feature,
        }


class TitleOpts:
    def __init__(
        self,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        title_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        subtitle_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        if isinstance(title_textstyle_opts, TextStyleOpts):
            title_textstyle_opts = title_textstyle_opts.opts
        if isinstance(subtitle_textstyle_opts, TextStyleOpts):
            subtitle_textstyle_opts = subtitle_textstyle_opts.opts

        self.opts: List = [
            {
                "text": title,
                "subtext": subtitle,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "bottom": pos_bottom,
                "textStyle": title_textstyle_opts,
                "subtextStyle": subtitle_textstyle_opts,
            }
        ]


class DataZoomOpts:
    def __init__(
        self,
        is_show: bool = True,
        type_: str = "slider",
        range_start: Numeric = 20,
        range_end: Numeric = 80,
        orient: str = "horizontal",
        xaxis_index: int = 0,
        yaxis_index: int = 0,
    ):
        self.opts: dict = {
            "show": is_show,
            "type": type_,
            "start": range_start,
            "end": range_end,
            "orient": orient,
            "xAxisIndex": xaxis_index,
            "yAxisIndex": yaxis_index,
        }


class LegendOpts:
    def __init__(
        self,
        selected_mode: Optional[str] = None,
        is_show: bool = True,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        orient: Optional[str] = None,
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        if isinstance(textstyle_opts, TextStyleOpts):
            textstyle_opts = textstyle_opts.opts

        self.opts: dict = {
            "selectedMode": selected_mode,
            "show": is_show,
            "left": pos_left,
            "right": pos_right,
            "top": pos_top,
            "bottom": pos_bottom,
            "orient": orient,
            "textStyle": textstyle_opts,
        }


class VisualMapOpts:
    def __init__(
        self,
        type_: str = "color",
        min_: Union[int, float] = 0,
        max_: Union[int, float] = 100,
        range_text: Union[list, tuple] = None,
        range_color: Union[List[str]] = None,
        range_size: Union[List[int]] = None,
        orient: str = "vertical",
        pos_left: str = "left",
        pos_top: str = "bottom",
        split_number: int = 5,
        dimension=None,
        is_calculable: bool = True,
        is_piecewise: bool = False,
        pieces=None,
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        if isinstance(textstyle_opts, TextStyleOpts):
            textstyle_opts = textstyle_opts.opts
        _inrange_op = {}
        if type_ == "color":
            range_color = range_color or ["#50a3ba", "#eac763", "#d94e5d"]
            _inrange_op.update(color=range_color)
        elif type_ == "size":
            range_size = range_size or [20, 50]
            _inrange_op.update(symbolSize=range_size)

        _visual_typ = "piecewise" if is_piecewise else "continuous"

        self.opts: dict = {
            "type": _visual_typ,
            "min": min_,
            "max": max_,
            "text": range_text,
            "textStyle": textstyle_opts,
            "inRange": _inrange_op,
            "calculable": is_calculable,
            "splitNumber": split_number,
            "dimension": dimension,
            "orient": orient,
            "left": pos_left,
            "top": pos_top,
            "showLabel": True,
        }
        if is_piecewise:
            self.opts.update(pieces=pieces)


class TooltipOpts:
    def __init__(
        self,
        trigger: str = "item",
        trigger_on: str = "mousemove|click",
        axis_pointer_type: str = "line",
        formatter: Optional[str] = None,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: Numeric = 0,
        textstyle_opts: TextStyleOpts = TextStyleOpts(font_size=14),
    ):
        if isinstance(textstyle_opts, TextStyleOpts):
            textstyle_opts = textstyle_opts.opts

        self.opts: dict = {
            "trigger": trigger,
            "triggerOn": trigger_on,
            "axisPointer": {"type": axis_pointer_type},
            "formatter": formatter,
            "textStyle": textstyle_opts,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
        }


class AxisOpts:
    def __init__(
        self,
        name: Optional[str] = None,
        is_show: bool = True,
        is_scale: bool = False,
        name_location: str = "end",
        name_gap: Numeric = 15,
        interval: Optional[Numeric] = None,
        grid_index: Numeric = 0,
        position: Optional[str] = None,
        boundary_gap: Optional[str] = None,
        label_alignment: Optional[str] = None,
        formatter: Optional[str] = None,
        inverse: Optional[str] = None,
        min_: Optional[Numeric] = None,
        max_: Optional[Numeric] = None,
        type_: Optional[str] = None,
        name_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(),
        linestyle_opts: Union[LineStyleOpts, dict] = LineStyleOpts(),
    ):
        if isinstance(name_textstyle_opts, TextStyleOpts):
            name_textstyle_opts = name_textstyle_opts.opts
        if isinstance(splitline_opts, SplitLineOpts):
            splitline_opts = splitline_opts.opts
        if isinstance(linestyle_opts, LineStyleOpts):
            linestyle_opts = linestyle_opts.opts

        self.opts: dict = {
            "name": name,
            "show": is_show,
            "scale": is_scale,
            "nameLocation": name_location,
            "nameGap": name_gap,
            "interval": interval,
            "nameTextStyle": name_textstyle_opts,
            "gridIndex": grid_index,
            "axisTick": {"alignWithLabel": label_alignment},
            "axisLabel": {"formatter": formatter},
            "inverse": inverse,
            "position": position,
            "boundaryGap": boundary_gap,
            "min": min_,
            "max": max_,
            "type": type_,
            "splitLine": splitline_opts,
            "axisLine": {"lineStyle": linestyle_opts},
        }


class GridOpts:
    def __init__(
        self,
        pos_left: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        width: Optional[Numeric] = None,
        height: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "left": pos_left,
            "top": pos_top,
            "right": pos_right,
            "bottom": pos_bottom,
            "width": width,
            "height": height,
        }


class Grid3DOpts:
    def __init__(
        self,
        width: Numeric = 200,
        height: Numeric = 100,
        depth: Numeric = 80,
        is_rotate: bool = False,
        rotate_speed: Numeric = 10,
        rotate_sensitivity: Numeric = 1,
    ):
        self.opts: dict = {
            "boxWidth": width,
            "boxHeight": height,
            "boxDepth": depth,
            "viewControl": {
                "autoRotate": is_rotate,
                "autoRotateSpeed": rotate_speed,
                "rotateSensitivity": rotate_sensitivity,
            },
        }


class Axis3DOpts:
    def __init__(
        self,
        data: Sequence = None,
        type_: Optional[str] = None,
        name: Optional[str] = None,
        name_size: Numeric = 16,
        name_gap: Numeric = 20,
        min_=None,
        max_=None,
        interval: Optional[str] = None,
        margin: Numeric = 8,
    ):
        self.opts: dict = {
            "data": data,
            "name": name,
            "nameGap": name_gap,
            "nameTextStyle": {"fontSize": name_size},
            "type": type_,
            "min": min_,
            "max": max_,
            "axisLabel": {"margin": margin, "interval": interval},
        }


class ParallelOpts:
    def __init__(
        self,
        pos_left: str = "5%",
        pos_right: str = "13%",
        pos_bottom: str = "10%",
        pos_top: str = "20%",
        layout: Optional[str] = None,
    ):
        self.opts: dict = {
            "left": pos_left,
            "right": pos_right,
            "bottom": pos_bottom,
            "top": pos_top,
            "layout": layout,
        }


class ParallelAxisOpts:
    def __init__(
        self,
        dim: Numeric,
        name: str,
        data: Sequence = None,
        type_: Optional[str] = None,
        min_: Union[str, Numeric, None] = None,
        max_: Union[str, Numeric, None] = None,
        is_scale: bool = False,
    ):
        self.opts: dict = {
            "dim": dim,
            "name": name,
            "data": data,
            "type": type_,
            "min": min_,
            "max": max_,
            "scale": is_scale,
        }


class RadarIndicatorOpts:
    def __init__(
        self,
        name: Optional[str] = None,
        min_: Optional[Numeric] = None,
        max_: Optional[Numeric] = None,
        color: Optional[str] = None,
    ):
        self.opts: dict = {"name": name, "max": max_, "min": min_, "color": color}


class CalendarOpts:
    def __init__(
        self,
        pos_left: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        orient: Optional[str] = None,
        range_: Union[str, Sequence, int] = None,
        daylabel_opts: Union[LabelOpts, dict, None] = None,
        monthlabel_opts: Union[LabelOpts, dict, None] = None,
        yearlabel_opts: Union[LabelOpts, dict, None] = None,
    ):
        if isinstance(daylabel_opts, LabelOpts):
            daylabel_opts = daylabel_opts.opts
        if isinstance(monthlabel_opts, LabelOpts):
            monthlabel_opts = monthlabel_opts.opts
        if isinstance(yearlabel_opts, LabelOpts):
            yearlabel_opts = yearlabel_opts.opts

        self.opts: dict = {
            "left": pos_left,
            "top": pos_top,
            "right": pos_right,
            "bottom": pos_bottom,
            "orient": orient,
            "range": range_,
            "dayLabel": daylabel_opts,
            "monthLabel": monthlabel_opts,
            "yearLabel": yearlabel_opts,
        }


class SingleAxisOpts:
    def __init__(
        self,
        name: Optional[str] = None,
        max_: Union[str, Numeric, None] = None,
        min_: Union[str, Numeric, None] = None,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        width: Optional[str] = None,
        height: Optional[str] = None,
        orient: Optional[str] = None,
        type_: Optional[str] = None,
    ):
        self.opts: dict = {
            "name": name,
            "max": max_,
            "min": min_,
            "left": pos_left,
            "right": pos_right,
            "top": pos_top,
            "bottom": pos_bottom,
            "width": width,
            "height": height,
            "orient": orient,
            "type": type_,
        }
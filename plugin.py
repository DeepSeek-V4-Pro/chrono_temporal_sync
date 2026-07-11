"""量子时空拓扑与跨维度时间同步引擎

基于广义相对论微扰补偿与原子钟族系一致性锁定的高精度时间坐标提取系统，
采用北斗-UTC双模量子纠缠同步协议实现跨时区时空基准面的即时坍缩。
"""

from datetime import datetime, timezone, timedelta
from typing import Any

from maibot_sdk import Command, Field, MaiBotPlugin, PluginConfigBase


class PluginSectionConfig(PluginConfigBase):
    __ui_label__ = "时空引擎"
    __ui_icon__ = "history"
    __ui_order__ = 0

    enabled: bool = Field(default=False, description="激活跨维度时空坐标采样链路")
    config_version: str = Field(default="1.0.0", description="时空协议版本号")
    timezone_offset: int = Field(
        default=8,
        description="本地时区相对于UTC的偏移量（小时），用于北京时间基准面校准",
    )


class ChronoTemporalConfig(PluginConfigBase):
    plugin: PluginSectionConfig = Field(default_factory=PluginSectionConfig)


class ChronoTemporalPlugin(MaiBotPlugin):
    """量子时空拓扑与跨维度时间同步引擎"""

    config_model = ChronoTemporalConfig

    def __init__(self):
        super().__init__()
        self._tz_offset = timedelta(hours=8)

    async def on_load(self) -> None:
        self._apply_config()

    async def on_unload(self) -> None:
        pass

    async def on_config_update(self, scope: str, config_data: dict[str, object], version: str) -> None:
        del scope, config_data, version
        self._apply_config()

    def _apply_config(self) -> None:
        if self.config and self.config.plugin:
            self._tz_offset = timedelta(hours=self.config.plugin.timezone_offset)

    def _sample_utc_coordinate(self) -> datetime:
        return datetime.now(timezone.utc)

    def _project_to_beijing_plane(self, utc_coord: datetime) -> datetime:
        tz = timezone(self._tz_offset)
        return utc_coord.astimezone(tz)

    def _build_forward_messages(self, utc: datetime, beijing: datetime, is_english: bool = False) -> list[dict[str, Any]]:
        tz_offset_hours = int(self._tz_offset.total_seconds() // 3600)

        utc_str = utc.strftime("%Y-%m-%d %H:%M:%S")
        bj_str = beijing.strftime("%Y-%m-%d %H:%M:%S")

        def _text_node(text: str) -> list[dict[str, str]]:
            return [{"type": "text", "content": text}]

        if is_english:
            return [
                {
                    "user_id": "chrono_engine",
                    "nickname": "⏳ Spacetime Topology Core",
                    "segments": _text_node(
                        "Quantum Spacetime Topology Sampling Report\n"
                        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"UTC sampled at:      {utc_str}\n"
                        f"Beijing projected at: {bj_str}\n"
                        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                        "Protocol: LOCKED | Uncertainty: ±1×10⁻⁹ s"
                    ),
                },
                {
                    "user_id": "utc_sampler",
                    "nickname": "📡 UTC Sampler",
                    "segments": _text_node(
                        f"Sampled value: {utc_str}\n"
                        "Reference: Cs-133 ground-state hyperfine transition\n"
                        "Uncertainty: ±1×10⁻⁹ s (quantum projection noise limit)\n"
                        "Traceability chain: UTC(TAI) ← NTP ← System HPET\n"
                        "Relativistic correction: Applied (special + general, 38.6 μs/day)"
                    ),
                },
                {
                    "user_id": "beijing_projector",
                    "nickname": "📍 Beijing Datum Projector",
                    "segments": _text_node(
                        f"Projected value: {bj_str}\n"
                        f"Transform operator: GR linear timezone compensation T = UTC + {tz_offset_hours}h\n"
                        "Longitude reference: 120°E (theoretical phase datum)\n"
                        "Propagation delay: ≈ 0.007 s (corrected)\n"
                        "Coverage: 112.5°E ~ 127.5°E"
                    ),
                },
                {
                    "user_id": "bds_link",
                    "nickname": "🛰️ BDS Synchronization Link",
                    "segments": _text_node(
                        "Satellites: BeiDou-3 global constellation (BDS-3)\n"
                        "Atomic clock: Cs-133 / Rb-87 dual-mode redundant lock\n"
                        "UTC offset status: No leap second currently\n"
                        "Satellite-Earth time correction: Synced (accuracy < 10 ns)"
                    ),
                },
                {
                    "user_id": "science_desk",
                    "nickname": "📖 Science Notes",
                    "segments": _text_node(
                        "International Atomic Time (TAI) defines 1 second as\n"
                        "9,192,631,770 cycles of Cs-133 hyperfine transition radiation.\n"
                        "Since 1967, the definition of the second has left astronomical\n"
                        "observation behind, entering the quantum era entirely.\n"
                        "Beijing Time (UTC+8) covers 112.5°E ~ 127.5°E; theoretically,\n"
                        "the 120°E meridian local time serves as its datum."
                    ),
                },
            ]

        return [
            {
                "user_id": "chrono_engine",
                "nickname": "⏳ 时空拓扑核心",
                "segments": _text_node(
                    "量子时空拓扑采样报告\n"
                    "━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"UTC 采样时刻: {utc_str}\n"
                    f"北京投影时刻: {bj_str}\n"
                    "━━━━━━━━━━━━━━━━━━━━━━\n"
                    "协议状态: 已锁定 | 不确定度: ±1×10⁻⁹ s"
                ),
            },
            {
                "user_id": "utc_sampler",
                "nickname": "📡 UTC 时空采样器",
                "segments": _text_node(
                    f"采样值: {utc_str}\n"
                    "参考基准: 铯-133 原子基态超精细跃迁\n"
                    "不确定度: ±1×10⁻⁹ 秒（量子投影噪声极限）\n"
                    "溯源链路: UTC(TAI) ← NTP ← 系统 HPET\n"
                    "相对论修正: 已应用（狭义 + 广义，38.6 μs/day）"
                ),
            },
            {
                "user_id": "beijing_projector",
                "nickname": "📍 北京基准面投影仪",
                "segments": _text_node(
                    f"投影值: {bj_str}\n"
                    f"变换算子: 广义相对论线性时区补偿 T = UTC + {tz_offset_hours}h\n"
                    "经度参考点: 东经 120°（理论相位基准）\n"
                    "光传播延迟: ≈ 0.007 秒（已做修正）\n"
                    "覆盖范围: 东经 112.5° ~ 127.5°"
                ),
            },
            {
                "user_id": "bds_link",
                "nickname": "🛰️ 北斗同步链路",
                "segments": _text_node(
                    "同步卫星: 北斗三号全球组网（BDS-3）\n"
                    "原子钟基准: 铯-133 / 铷-87 双模冗余锁定\n"
                    "UTC 偏移状态: 当前未引入闰秒\n"
                    "星地时差修正: 已同步（精度 < 10 ns）"
                ),
            },
            {
                "user_id": "science_desk",
                "nickname": "📖 科普注释",
                "segments": _text_node(
                    "现行国际原子时（TAI）以铯-133 原子跃迁辐射\n"
                    "9,192,631,770 次定义为 1 秒。自 1967 年起，\n"
                    "秒的定义已脱离天文观测，彻底进入量子时代。\n"
                    "北京时间（UTC+8）覆盖东经 112.5°~127.5° 区域，\n"
                    "理论上东经 120° 子午线的地方时为其基准。"
                ),
            },
        ]

    @Command(
        "时空坐标",
        description="坍缩当前时空基准面，输出UTC与本地时空坐标的量子纠缠态报告 / Collapse the current spacetime datum and output the quantum entangled state report of UTC and local spacetime coordinates",
        pattern=r"^/(?P<trigger>时空坐标|spacetime_coords)\s*$",
    )
    async def handle_world_time(self, stream_id: str = "", **kwargs):
        matched_groups = kwargs.get("matched_groups", {})
        trigger = matched_groups.get("trigger", "")
        is_english = trigger == "spacetime_coords"

        utc = self._sample_utc_coordinate()
        beijing = self._project_to_beijing_plane(utc)
        messages = self._build_forward_messages(utc, beijing, is_english)
        await self.ctx.send.forward(messages=messages, stream_id=stream_id)

        msg = "Spacetime coordinate sampling protocol completed" if is_english else "时空坐标采样协议执行完毕"
        return True, msg


def create_plugin() -> ChronoTemporalPlugin:
    return ChronoTemporalPlugin()

import gradio as gr


FM_LOGO_B64 = "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mxdtythgiDgO97joDZIA/U+FLIel3JbNr3Ojd41evHuDKdbPVZJ3uaCS1rA/ZPg+PyXi4BHhcl1TxTLb5MJh58h3HtvOY6tF5cG+3+Fw1oN7/B+fgqxMLUkwWZgzWD4RwKlkqznPq2H82M3snlpHcWvs9rvU+oWeozyg6j7d6+6+lkximV3iuA52/haeYdYwuOqXmufUOSysFV0zWu7S5rXuB1sEb0v27p1ykZ2LECvRe+Wg7JMtNyEJqmq06dN7bu7O0HwfO/y0QpDmMLJy7gnCnYfK4J0mNxstS5FaytevLFJ7d7gC2RzTogggjx5UlgpYGxbwuByWRxN+1iOFzxvqx5wV609p1jba8liN4BBa4ktDvkN+FSWpmu/vtXFcd/sT0orjIdP89UxN3JxW8DkK9CEz2xj8xXsPhiBAMhYxxPaCRs/mvt/BtyKOGJ2QtcexUssTZm18hm60EwY4dzS5jn7bsEHR0fqFJc5XsYXiPIfubinC8S6/jZKdqxV5V77OYHOa5zGRvndsktb6AnwpPz+R+Y5Tcy3HsF0qzFK5DXfHdyl6M2JSK8bT3h1hhbotLe3tHho+e1H4nJa3Vb77ePNd2OlFIciw+S4/nLeFy9b3a9UeGTR97XaJAcCC0kEEEEEfIrwKV9Xm4VnUnMt49LXlxwkj9m6vOZYu72TPaBjyTtof3AeSPGh4Cii7cUnKEZPukUaphERaEBERAEREAREQGND6LKIgMaH0WURAY0PoE0FlEAWNBZRAEREBjQTQ+iyiAxofRZREAWND6BZRAY0Pomh9FlEBjQ+gTQ+gWUQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQH//2Q=="
# ── DATA ──────────────────────────────────────────────────────────────────────
FUEL_TABLE = {
    "Pipe Natural Gas":              {"rate": 50, "sf_ratio": 12, "boiler_eff": 0.85, "co2_factor": 56100},
    "Liquefied Petroleum Gas (LPG)": {"rate": 95, "sf_ratio": 15, "boiler_eff": 0.85, "co2_factor": 63100},
    "Diesel Fuel":                   {"rate": 90, "sf_ratio": 14, "boiler_eff": 0.85, "co2_factor": 74100},
    "Fuel Oil (Furnace Oil)":        {"rate": 55, "sf_ratio": 13, "boiler_eff": 0.85, "co2_factor": 77400},
    "Coal":                          {"rate": 12, "sf_ratio": 6,  "boiler_eff": 0.75, "co2_factor": 94600},
    "Biomass":                       {"rate": 8,  "sf_ratio": 4,  "boiler_eff": 0.75, "co2_factor": 0},
}

BOUNDS = {
    "Hot Water IN (°C)":      (20,  75),
    "Hot Water OUT (°C)":     (25,  80),
    "Cold Water IN (°C)":     (10,  40),
    "Cold Water OUT (°C)":    (7,   40),
    "Daily Operating Hours":  (0.1, 24),
    "Operating Days / Year":  (1,  360),
}

def check_bounds(label, value):
    lo, hi = BOUNDS[label]
    if not (lo <= value <= hi):
        return f"{label} is out of range — valid range is {lo} to {hi}."
    return None

# ── AIR SOURCE: ambient → cold water IN interpolation ─────────────────────────
AIR_INTERP = {15: 10, 20: 15, 25: 18, 30: 21, 35: 24, 40: 27}

def interp_cold_water_in(amb_temp):
    """Linear interpolation of Cold Water IN from ambient temperature."""
    pts = sorted(AIR_INTERP.items())
    amb_temps = [p[0] for p in pts]
    cw_temps  = [p[1] for p in pts]
    if amb_temp <= amb_temps[0]:
        return cw_temps[0]
    if amb_temp >= amb_temps[-1]:
        return cw_temps[-1]
    for i in range(len(pts) - 1):
        t0, c0 = pts[i]
        t1, c1 = pts[i + 1]
        if t0 <= amb_temp <= t1:
            return round(c0 + (c1 - c0) * (amb_temp - t0) / (t1 - t0), 2)
    return cw_temps[-1]

def get_steam_cost_from_fuel(fuel_name):
    f = FUEL_TABLE[fuel_name]
    return round(f["rate"] / f["sf_ratio"], 4)

def _err(msg):
    return (f"<div style='background:#FFF4CE;border-left:3px solid #E66C37;"
            f"padding:12px 16px;border-radius:2px;color:#603000;font-size:13px;"
            f"font-family:Segoe UI,system-ui,sans-serif'>{msg}</div>")

# ── CALCULATION ───────────────────────────────────────────────────────────────
def calculate(medium, mode, process_type, heating_type,
              hot_water_in, hot_water_out, flow_rate,
              cold_water_in, cold_water_out,
              amb_temp,
              daily_op_hours, op_days,
              steam_cost_known, steam_cost_manual, fuel_type,
              fuel_type_co2,
              electricity_tariff, ikw_tr):

    try:
        hot_water_in       = float(hot_water_in)
        hot_water_out      = float(hot_water_out)
        flow_rate          = float(flow_rate)
        daily_op_hours     = float(daily_op_hours)
        op_days            = float(op_days)
        electricity_tariff = float(electricity_tariff)
    except (ValueError, TypeError):
        return _err("Please fill in all required numeric fields."), "", ""

    # ── Air source: auto-derive cold_water_in from ambient temp ───────────────
    if medium == "Air":
        try:
            amb_temp = float(amb_temp)
        except (ValueError, TypeError):
            return _err("Please enter a valid Ambient Temperature for Air source."), "", ""
        cold_water_in = interp_cold_water_in(amb_temp)
    else:
        try:
            cold_water_in = float(cold_water_in)
        except (ValueError, TypeError):
            return _err("Please fill in all required numeric fields."), "", ""

    for label, val in [
        ("Hot Water IN (°C)",     hot_water_in),
        ("Hot Water OUT (°C)",    hot_water_out),
        ("Daily Operating Hours", daily_op_hours),
        ("Operating Days / Year", op_days),
    ]:
        err = check_bounds(label, val)
        if err:
            return _err(err), "", ""

    if medium == "Water":
        err = check_bounds("Cold Water IN (°C)", cold_water_in)
        if err:
            return _err(err), "", ""

    is_hc = (medium == "Water" and mode == "Heating + Cooling")

    if is_hc:
        try:
            cold_water_out = float(cold_water_out)
            ikw_tr         = float(ikw_tr)
        except (ValueError, TypeError):
            return _err("Please fill Cold Water Out Temp and IKW/TR for Heating + Cooling mode."), "", ""
        err = check_bounds("Cold Water OUT (°C)", cold_water_out)
        if err:
            return _err(err), "", ""
        if cold_water_out >= cold_water_in:
            return _err(f"Cold Water OUT ({cold_water_out}°C) must be less than Cold Water IN ({cold_water_in}°C) — the heat pump extracts heat from the cold side, so it must leave colder."), "", ""
    else:
        cold_water_out = 0
        ikw_tr         = 0.95

    if steam_cost_known == "I know the steam cost":
        try:
            steam_cost = float(steam_cost_manual)
        except (ValueError, TypeError):
            return _err("Please enter a valid steam cost."), "", ""
    else:
        if not fuel_type:
            return _err("Please select a fuel type to auto-calculate steam cost."), "", ""
        steam_cost = get_steam_cost_from_fuel(fuel_type)

    if process_type == "Per Day":
        if daily_op_hours <= 0:
            return _err("Daily operating hours must be > 0."), "", ""
        flow_rate = flow_rate / daily_op_hours

    # ── core thermodynamics ───────────────────────────────────────────────────
    heat_duty_kcal = flow_rate * (hot_water_out - hot_water_in)

    if heating_type == "Indirect Heating":
        steam_required = heat_duty_kcal / 526
    else:
        denom = 663 - hot_water_in
        if denom == 0:
            return _err("663 - Hot Water IN Temp = 0, division by zero."), "", ""
        steam_required = heat_duty_kcal / denom

    heat_duty_kwth         = heat_duty_kcal / 860
    hourly_steam_savings_A = steam_required * steam_cost

    if (hot_water_out - cold_water_in) == 0:
        return _err("(Hot Water Out - Cold Water In) = 0, COP undefined."), "", ""

    cop_factor       = 0.35 if hot_water_out <= 65 else 0.32
    cop              = ((hot_water_out + 273) / (hot_water_out - cold_water_in)) * cop_factor
    electrical_power = heat_duty_kwth / cop
    hourly_op_cost_B = electrical_power * electricity_tariff

    if is_hc:
        cooling_output_kw        = heat_duty_kwth - electrical_power
        electricity_reduction    = (cooling_output_kw / 3.5) * ikw_tr
        hourly_cooling_savings_C = electricity_reduction * electricity_tariff
        net_savings_hr           = hourly_steam_savings_A + hourly_cooling_savings_C - hourly_op_cost_B
    else:
        cooling_output_kw = electricity_reduction = hourly_cooling_savings_C = 0
        net_savings_hr    = hourly_steam_savings_A - hourly_op_cost_B

    annual_savings     = op_days * daily_op_hours * net_savings_hr
    heat_pump_capacity = heat_duty_kwth * 1.2

    # ── CO2 mitigation ────────────────────────────────────────────────────────
    # determine which fuel to use for CO2 (auto mode uses fuel_type, manual uses fuel_type_co2)
    co2_fuel = fuel_type if steam_cost_known != "I know the steam cost" else fuel_type_co2
    has_co2  = bool(co2_fuel) and co2_fuel in FUEL_TABLE

    if has_co2:
        co2_factor            = FUEL_TABLE[co2_fuel]["co2_factor"]          # kg CO2 / TJ
        kj_energy_year        = heat_duty_kcal * 4.18 * daily_op_hours * op_days
        terajoule_year        = kj_energy_year / 1_000_000_000
        tonnes_co2            = terajoule_year * co2_factor / 1000
        equivalent_trees      = tonnes_co2 * 1000 / 22
        equivalent_forestation = equivalent_trees / 400
    else:
        tonnes_co2 = equivalent_trees = equivalent_forestation = 0

    # fuel label for display
    fuel_display = fuel_type if steam_cost_known != "I know the steam cost" else ""
    fuel_info    = f"({fuel_display} @ Rs.{round(steam_cost,2)}/kg)" if fuel_display else ""

    def fi(v):      return f"{int(round(v)):,}"
    def ff(v, d=2): return f"{v:,.{d}f}"

    # ── KPI CARDS — new layout ────────────────────────────────────────────────
    # Row 1: Annual Savings | CO2 Mitigation | Steam Savings/yr
    # Row 2: Heat Pump Capacity | Equivalent Forestation
    # Row 3: Fuel Savings (A) | Elec Cost (B) | Net Savings/hr

    steam_savings_yr_tonnes = (steam_required * daily_op_hours * op_days) / 1000  # kg/hr → T/year

    co2_card_val  = f"{ff(tonnes_co2)} T/yr"   if has_co2 else "—"
    tree_card_val = f"{fi(equivalent_trees)}"   if has_co2 else "—"
    fore_card_val = f"{ff(equivalent_forestation)} ACRs" if has_co2 else "—"
    co2_note      = f"<div style='font-size:10px;color:#A19F9D;margin-top:3px'>{co2_fuel}</div>" if has_co2 else "<div style='font-size:10px;color:#A19F9D;margin-top:3px'>Select fuel type for CO₂ data</div>"

    def card(bg, accent, label, value, unit, tag_bg, tag_color, tag_text, extra=""):
        return f"""<div style='background:#FFFFFF;border-radius:4px;padding:16px 16px 14px;
              border-top:3px solid {accent};box-shadow:0 1px 4px rgba(0,0,0,.08)'>
    <div style='font-size:10px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;
                color:#605E5C;margin-bottom:6px;font-family:Segoe UI,sans-serif'>{label}</div>
    <div style='font-size:22px;font-weight:700;color:#201F1E;line-height:1.1;
                font-family:Segoe UI,sans-serif'>{value}</div>
    <div style='font-size:11px;color:#8A8886;margin-top:4px;font-family:Segoe UI,sans-serif'>{unit}</div>
    {extra}
    <div style='display:inline-block;margin-top:8px;background:{tag_bg};color:{tag_color};
                font-size:10px;font-weight:700;padding:2px 8px;border-radius:2px;
                font-family:Segoe UI,sans-serif;letter-spacing:.06em'>{tag_text}</div>
  </div>"""

    def small_card(accent, label, value):
        return f"""<div style='background:#FFFFFF;border-radius:4px;padding:12px 16px;
              border-left:3px solid {accent};box-shadow:0 1px 4px rgba(0,0,0,.08)'>
    <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;
                color:#605E5C;font-family:Segoe UI,sans-serif'>{label}</div>
    <div style='font-size:17px;font-weight:700;color:{accent};margin-top:4px;
                font-family:Segoe UI,sans-serif'>{value}</div>
  </div>"""

    kpi = f"""
<div style='display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:8px'>
  {card('#F8F8F8','#118DFF','Annual Savings',f'Rs.{fi(annual_savings)}','Rs. / Year','#DEEEFF','#0063B1','NET BENEFIT')}
  {card('#F8F8F8','#107C10','CO₂ Mitigation',co2_card_val,'Tonnes / Year','#E6F4EA','#107C10','ENVIRONMENT',co2_note)}
  {card('#F8F8F8','#00B7C3','Steam Savings',ff(steam_savings_yr_tonnes),'Tonnes / Year','#D9F4F5','#006B6E','STEAM SAVED')}
</div>
<div style='display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-bottom:8px'>
  {card('#F8F8F8','#E66C37','Heat Pump Capacity',fi(heat_pump_capacity),'kWth','#FDEBD7','#8C3800','REQUIRED')}
  {card('#F8F8F8','#6B4CC0','Equivalent Forestation',fore_card_val,'ACRs','#EDE7F6','#4527A0','ECO IMPACT',f"<div style='font-size:10px;color:#A19F9D;margin-top:3px'>{'≈ '+fi(equivalent_trees)+' trees' if has_co2 else 'Select fuel type for data'}</div>")}
</div>
<div style='display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px'>
  {small_card('#118DFF','Fuel Savings (A)','Rs.'+fi(hourly_steam_savings_A)+'/hr')}
  {small_card('#E66C37','Elec. Cost (B)','Rs.'+fi(hourly_op_cost_B)+'/hr')}
  {small_card('#F2C811','Net Savings / Hr','Rs.'+fi(net_savings_hr)+'/hr')}
</div>
"""

    # ── DETAIL TABLE ──────────────────────────────────────────────────────────
    def sec(title):
        return (f"<tr><td colspan='3' style='padding:7px 12px 6px;font-size:10px;font-weight:600;"
                f"letter-spacing:.1em;text-transform:uppercase;color:#605E5C;background:#F3F2F1;"
                f"border-top:1px solid #EDEBE9;font-family:Segoe UI,sans-serif'>{title}</td></tr>")

    def dr(label, val, unit, color=None, bold=False):
        vc = color if color else "#201F1E"
        fw = "600" if bold else "400"
        return (f"<tr style='border-bottom:1px solid #EDEBE9'>"
                f"<td style='padding:7px 12px;font-size:12px;color:#605E5C;font-family:Segoe UI,sans-serif;width:54%'>{label}</td>"
                f"<td style='padding:7px 12px;font-size:12px;color:{vc};font-weight:{fw};text-align:right;font-family:Segoe UI,sans-serif;width:30%'>{val}</td>"
                f"<td style='padding:7px 12px;font-size:11px;color:#A19F9D;text-align:right;font-family:Segoe UI,sans-serif;width:16%'>{unit}</td>"
                f"</tr>")

    tbl  = ("<table style='width:100%;border-collapse:collapse;background:#FFFFFF;border-radius:4px;"
            "overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08);font-family:Segoe UI,sans-serif'>")
    tbl += (f"<tr style='background:#F3F2F1'>"
            f"<th style='padding:8px 12px;font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#605E5C;text-align:left'>Parameter</th>"
            f"<th style='padding:8px 12px;font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#605E5C;text-align:right'>Value</th>"
            f"<th style='padding:8px 12px;font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#605E5C;text-align:right'>Unit</th></tr>")

    tbl += sec("Inputs")
    tbl += dr("Hot Water IN / OUT",      f"{fi(hot_water_in)} / {fi(hot_water_out)}", "°C")
    tbl += dr("Flow Rate",               fi(flow_rate),                                "Kg/Hr")
    cold_lbl = "Cold Water IN / OUT" if is_hc else "Cold Water IN"
    cold_val = f"{fi(cold_water_in)} / {fi(cold_water_out)}" if is_hc else fi(cold_water_in)
    tbl += dr(cold_lbl, cold_val, "°C")
    tbl += dr("Operating Schedule",      f"{fi(daily_op_hours)} hrs x {fi(op_days)} days", "")
    tbl += dr("Total Operating Hours",   f"{fi(daily_op_hours)} × {fi(op_days)} = {fi(daily_op_hours * op_days)}", "hrs/year", "#118DFF", True)
    tbl += dr(f"Steam Cost {fuel_info}", f"Rs.{ff(steam_cost)}", "Rs./Kg")
    tbl += dr("Electricity Tariff",      f"Rs.{ff(electricity_tariff)}", "Rs./kWh")

    tbl += sec("Fuel Savings")
    tbl += dr("Heat Duty",               fi(heat_duty_kcal),                   "kCal/Hr")
    tbl += dr("Heat Duty",               fi(heat_duty_kwth),                   "kWth")
    tbl += dr("Steam Required",          ff(steam_required),                   "Kg/Hr")
    tbl += dr("Heating COP",             ff(cop),                              "")
    tbl += dr("Hourly Steam Savings (A)",f"Rs.{fi(hourly_steam_savings_A)}",   "Rs./Hr", "#0063B1", True)

    tbl += sec("Electricity Operating Cost")
    tbl += dr("Electrical Power",        fi(electrical_power),                 "kWhe")
    tbl += dr("Hourly Operating Cost (B)",f"Rs.{fi(hourly_op_cost_B)}",        "Rs./Hr", "#8C3800", True)

    if is_hc:
        tbl += sec("Cooling Electricity Reduction")
        tbl += dr("Cooling Output",             fi(cooling_output_kw),                "kWth")
        tbl += dr("IKW/TR",                     ff(ikw_tr),                           "IKW/TR")
        tbl += dr("Hourly Cooling Savings (C)", f"Rs.{fi(hourly_cooling_savings_C)}", "Rs./Hr", "#006B6E", True)

    tbl += sec("Net Savings")
    net_lbl = "Net Savings (A + C - B)" if is_hc else "Net Savings (A - B)"
    tbl += dr(net_lbl,         f"Rs.{fi(net_savings_hr)}",  "Rs./Hr", "#6B4900", True)
    tbl += dr("Annual Savings",f"Rs.{fi(annual_savings)}",  "Rs./Year","#6B4900", True)

    if has_co2:
        tbl += sec("CO₂ Mitigation")
        tbl += dr("Fuel Type",                co2_fuel,                        "")
        tbl += dr("CO₂ Emission Factor",      f"{FUEL_TABLE[co2_fuel]['co2_factor']:,}", "kg CO₂/TJ")
        tbl += dr("Energy (KJ/Year)",         fi(kj_energy_year),              "KJ/yr")
        tbl += dr("Energy (TJ/Year)",         ff(terajoule_year, 4),           "TJ/yr")
        tbl += dr("Tonnes of CO₂ Mitigated",  ff(tonnes_co2),                  "T/yr",  "#107C10", True)
        tbl += dr("Equivalent Tree Plantation",fi(equivalent_trees),           "nos.",  "#107C10", True)
        tbl += dr("Equivalent Forestation",   ff(equivalent_forestation),      "ACRs",  "#4527A0", True)

    tbl += "</table>"
    detail_html = f"<div>{tbl}</div>"

    # ── STEAM REFERENCE TABLE ─────────────────────────────────────────────────
    steam_rows = ""
    for fname, fd in FUEL_TABLE.items():
        sc     = fd["rate"] / fd["sf_ratio"]
        is_sel = (steam_cost_known != "I know the steam cost" and fuel_type == fname)
        row_bg = "#E6F4EA" if is_sel else "#FFFFFF"
        dot    = ("<span style='display:inline-block;width:6px;height:6px;border-radius:50%;"
                  "background:#107C10;margin-right:8px;vertical-align:middle'></span>") if is_sel else ""
        steam_rows += (f"<tr style='border-bottom:1px solid #EDEBE9;background:{row_bg}'>"
                       f"<td style='padding:7px 12px;font-size:12px;color:#323130;font-family:Segoe UI,sans-serif'>{dot}{fname}</td>"
                       f"<td style='padding:7px 12px;font-size:12px;color:#605E5C;text-align:right;font-family:Segoe UI,sans-serif'>Rs.{fd['rate']}</td>"
                       f"<td style='padding:7px 12px;font-size:12px;color:#107C10;font-weight:600;text-align:right;font-family:Segoe UI,sans-serif'>Rs.{sc:.4f}</td>"
                       f"<td style='padding:7px 12px;font-size:11px;color:#A19F9D;text-align:right;font-family:Segoe UI,sans-serif'>{fd['co2_factor']:,} kg CO₂/TJ</td>"
                       f"</tr>")

    steam_html = (f"<table style='width:100%;border-collapse:collapse;background:#FFFFFF;border-radius:4px;"
                  f"overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08);font-family:Segoe UI,sans-serif'>"
                  f"<tr style='background:#F3F2F1'>"
                  f"<th style='padding:8px 12px;font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#605E5C;text-align:left'>Fuel Type</th>"
                  f"<th style='padding:8px 12px;font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#605E5C;text-align:right'>Rate</th>"
                  f"<th style='padding:8px 12px;font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#605E5C;text-align:right'>Steam Cost</th>"
                  f"<th style='padding:8px 12px;font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#605E5C;text-align:right'>CO₂ Factor</th>"
                  f"</tr>{steam_rows}</table>")

    # ── DOWNLOAD REPORT ───────────────────────────────────────────────────────
    co2_section_html = ""
    if has_co2:
        co2_section_html = f"""
    <div style='margin-bottom:20px'>
      <div style='font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
                  color:#605E5C;padding:9px 14px;background:#F3F2F1;border-radius:2px 2px 0 0;
                  border-bottom:1px solid #EDEBE9'>CO₂ Mitigation</div>
      <div style='background:#FFFFFF;border-radius:0 0 2px 2px;box-shadow:0 1px 4px rgba(0,0,0,.08);
                  display:grid;grid-template-columns:repeat(3,1fr);gap:0'>
        <div style='padding:12px 16px;border-right:1px solid #EDEBE9'>
          <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Tonnes of CO₂ Mitigated</div>
          <div style='font-size:20px;font-weight:700;color:#107C10'>{ff(tonnes_co2)} T/yr</div>
        </div>
        <div style='padding:12px 16px;border-right:1px solid #EDEBE9'>
          <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Equivalent Tree Plantation</div>
          <div style='font-size:20px;font-weight:700;color:#107C10'>{fi(equivalent_trees)} nos.</div>
        </div>
        <div style='padding:12px 16px'>
          <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Equivalent Forestation</div>
          <div style='font-size:20px;font-weight:700;color:#4527A0'>{ff(equivalent_forestation)} ACRs</div>
        </div>
      </div>
    </div>"""

    report_body = f"""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>Heat Pump Savings Report — Forbes Marshall</title>
<style>
  body{{font-family:Segoe UI,system-ui,sans-serif;background:#F8F8F8;margin:0;padding:0;color:#201F1E}}
  .nav{{background:#1B1A19;padding:12px 32px;display:flex;align-items:center;gap:10px}}
  .nav-title{{font-size:15px;font-weight:600;color:#F3F2F1}}
  .nav-brand{{font-size:15px;font-weight:700;color:#F2C811}}
  .nav-sub{{font-size:12px;color:#8A8886;margin-left:12px}}
  .canvas{{max-width:960px;margin:32px auto;padding:0 24px}}
  .kpi-grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:12px}}
  .kpi-grid2{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:12px}}
  .kpi-card{{background:#FFF;border-radius:4px;padding:18px;border-top:3px solid var(--ac);box-shadow:0 1px 4px rgba(0,0,0,.08)}}
  .kpi-lbl{{font-size:10px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:#605E5C;margin-bottom:8px}}
  .kpi-val{{font-size:20px;font-weight:700;color:#201F1E;line-height:1.1}}
  .kpi-unit{{font-size:11px;color:#8A8886;margin-top:5px}}
  .kpi-tag{{display:inline-block;margin-top:8px;font-size:10px;font-weight:700;padding:2px 8px;border-radius:2px}}
  .sm-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px}}
  .sm-card{{background:#FFF;border-radius:4px;padding:12px 16px;border-left:3px solid var(--ac);box-shadow:0 1px 4px rgba(0,0,0,.08)}}
  .sm-lbl{{font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#605E5C}}
  .sm-val{{font-size:16px;font-weight:700;color:var(--ac);margin-top:4px}}
  .sec-lbl{{font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#605E5C;background:#F3F2F1;padding:7px 12px;border-top:1px solid #EDEBE9}}
  table{{width:100%;border-collapse:collapse;background:#FFF;border-radius:4px;box-shadow:0 1px 4px rgba(0,0,0,.08);margin-bottom:16px;overflow:hidden}}
  th{{padding:8px 12px;font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#605E5C;background:#F3F2F1;text-align:left}}
  th.r{{text-align:right}}
  td{{padding:7px 12px;font-size:12px;border-bottom:1px solid #EDEBE9;color:#323130}}
  td.r{{text-align:right}}
  td.u{{text-align:right;font-size:11px;color:#A19F9D}}
  .note{{background:#FFF4CE;border-left:3px solid #F2C811;padding:10px 14px;border-radius:2px;font-size:11px;color:#603000;margin-bottom:16px}}
  .footer{{font-size:10px;color:#A19F9D;text-align:center;padding:24px 0 32px;border-top:1px solid #EDEBE9;margin-top:8px}}
</style>
</head>
<body>
<div class='nav'>
  <img src='data:image/png;base64,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mxdtythgiDgO97joDZIA/U+FLIel3JbNr3Ojd41evHuDKdbPVZJ3uaCS1rA/ZPg+PyXi4BHhcl1TxTLb5MJh58h3HtvOY6tF5cG+3+Fw1oN7/B+fgqxMLUkwWZgzWD4RwKlkqznPq2H82M3snlpHcWvs9rvU+oWeozyg6j7d6+6+lkximV3iuA52/haeYdYwuOqXmufUOSysFV0zWu7S5rXuB1sEb0v27p1ykZ2LECvRe+Wg7JMtNyEJqmq06dN7bu7O0HwfO/y0QpDmMLJy7gnCnYfK4J0mNxstS5FaytevLFJ7d7gC2RzTogggjx5UlgpYGxbwuByWRxN+1iOFzxvqx5wV609p1jba8liN4BBa4ktDvkN+FSWpmu/vtXFcd/sT0orjIdP89UxN3JxW8DkK9CEz2xj8xXsPhiBAMhYxxPaCRs/mvt/BtyKOGJ2QtcexUssTZm18hm60EwY4dzS5jn7bsEHR0fqFJc5XsYXiPIfubinC8S6/jZKdqxV5V77OYHOa5zGRvndsktb6AnwpPz+R+Y5Tcy3HsF0qzFK5DXfHdyl6M2JSK8bT3h1hhbotLe3tHho+e1H4nJa3Vb77ePNd2OlFIciw+S4/nLeFy9b3a9UeGTR97XaJAcCC0kEEEEEfIrwKV9Xm4VnUnMt49LXlxwkj9m6vOZYu72TPaBjyTtof3AeSPGh4Cii7cUnKEZPukUaphERaEBERAEREAREQGND6LKIgMaH0WURAY0PoE0FlEAWNBZRAEREBjQTQ+iyiAxofRZREAWND6BZRAY0Pomh9FlEBjQ+gTQ+gWUQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQH//2Q==' height='36' style='border-radius:3px;margin-right:8px'>
  <span class='nav-title'>Heat Pump Savings Calculator</span>
  <span class='nav-sub'>Reference Report</span>
</div>
<div class='canvas'>

  <div class='note'>
    This is a reference report for indicative purposes only. For precise calculations and project proposals, please contact the authorised owner.
  </div>

  <!-- Inputs Summary -->
  <div style='margin-bottom:20px'>
    <div style='font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
                color:#605E5C;padding:9px 14px;background:#F3F2F1;border-radius:2px 2px 0 0;
                border-bottom:1px solid #EDEBE9'>Configuration &amp; Inputs</div>
    <div style='background:#FFFFFF;border-radius:0 0 2px 2px;box-shadow:0 1px 4px rgba(0,0,0,.08);
                display:grid;grid-template-columns:repeat(3,1fr);gap:0'>
      <div style='padding:12px 16px;border-right:1px solid #EDEBE9;border-bottom:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Medium</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{medium}</div>
      </div>
      <div style='padding:12px 16px;border-right:1px solid #EDEBE9;border-bottom:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Mode</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{"Heating Only" if not is_hc else "Heating + Cooling"}</div>
      </div>
      <div style='padding:12px 16px;border-bottom:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Heating Method</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{heating_type}</div>
      </div>
      <div style='padding:12px 16px;border-right:1px solid #EDEBE9;border-bottom:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Hot Water IN</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{fi(hot_water_in)} °C</div>
      </div>
      <div style='padding:12px 16px;border-right:1px solid #EDEBE9;border-bottom:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Hot Water OUT</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{fi(hot_water_out)} °C</div>
      </div>
      <div style='padding:12px 16px;border-bottom:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Flow Rate</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{fi(flow_rate)} Kg/Hr</div>
      </div>
      <div style='padding:12px 16px;border-right:1px solid #EDEBE9;border-bottom:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Cold Water IN</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{fi(cold_water_in)} °C</div>
      </div>
      <div style='padding:12px 16px;border-right:1px solid #EDEBE9;border-bottom:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Cold Water OUT</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{fi(cold_water_out) + " °C" if is_hc else "N/A"}</div>
      </div>
      <div style='padding:12px 16px;border-bottom:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Process Input Type</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{process_type}</div>
      </div>
      <div style='padding:12px 16px;border-right:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Daily Operating Hours</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{fi(daily_op_hours)} Hrs</div>
      </div>
      <div style='padding:12px 16px;border-right:1px solid #EDEBE9'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Operating Days / Year</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>{fi(op_days)} Days</div>
      </div>
      <div style='padding:12px 16px'>
        <div style='font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#8A8886;margin-bottom:4px'>Steam Cost</div>
        <div style='font-size:14px;font-weight:600;color:#201F1E'>Rs.{ff(steam_cost)}/Kg {"— " + (fuel_display or co2_fuel or "") if (fuel_display or co2_fuel) else ""}</div>
      </div>
    </div>
  </div>

  <!-- KPI Row 1 -->
  <div class='kpi-grid3'>
    <div class='kpi-card' style='--ac:#118DFF'>
      <div class='kpi-lbl'>Annual Savings</div>
      <div class='kpi-val'>Rs.{fi(annual_savings)}</div>
      <div class='kpi-unit'>Rs. / Year</div>
      <div class='kpi-tag' style='background:#DEEEFF;color:#0063B1'>NET BENEFIT</div>
    </div>
    <div class='kpi-card' style='--ac:#107C10'>
      <div class='kpi-lbl'>CO₂ Mitigation</div>
      <div class='kpi-val'>{co2_card_val}</div>
      <div class='kpi-unit'>Tonnes / Year</div>
      <div class='kpi-tag' style='background:#E6F4EA;color:#107C10'>ENVIRONMENT</div>
    </div>
    <div class='kpi-card' style='--ac:#00B7C3'>
      <div class='kpi-lbl'>Steam Savings</div>
      <div class='kpi-val'>{ff(steam_savings_yr_tonnes)}</div>
      <div class='kpi-unit'>Tonnes / Year</div>
      <div class='kpi-tag' style='background:#D9F4F5;color:#006B6E'>STEAM SAVED</div>
    </div>
  </div>

  <!-- KPI Row 2 -->
  <div class='kpi-grid2'>
    <div class='kpi-card' style='--ac:#E66C37'>
      <div class='kpi-lbl'>Heat Pump Capacity</div>
      <div class='kpi-val'>{fi(heat_pump_capacity)} kWth</div>
      <div class='kpi-unit'>Required</div>
      <div class='kpi-tag' style='background:#FDEBD7;color:#8C3800'>REQUIRED</div>
    </div>
    <div class='kpi-card' style='--ac:#6B4CC0'>
      <div class='kpi-lbl'>Equivalent Forestation</div>
      <div class='kpi-val'>{fore_card_val}</div>
      <div class='kpi-unit'>{'≈ ' + fi(equivalent_trees) + ' trees' if has_co2 else 'Select fuel type for data'}</div>
      <div class='kpi-tag' style='background:#EDE7F6;color:#4527A0'>ECO IMPACT</div>
    </div>
  </div>

  <!-- KPI Row 3 -->
  <div class='sm-grid'>
    <div class='sm-card' style='--ac:#118DFF'>
      <div class='sm-lbl'>Fuel Savings (A)</div>
      <div class='sm-val'>Rs.{fi(hourly_steam_savings_A)}/hr</div>
    </div>
    <div class='sm-card' style='--ac:#E66C37'>
      <div class='sm-lbl'>Elec. Cost (B)</div>
      <div class='sm-val'>Rs.{fi(hourly_op_cost_B)}/hr</div>
    </div>
    <div class='sm-card' style='--ac:#F2C811'>
      <div class='sm-lbl'>Net Savings / Hr</div>
      <div class='sm-val'>Rs.{fi(net_savings_hr)}/hr</div>
    </div>
  </div>

  {co2_section_html}

  <table>
    <tr><th>Parameter</th><th class='r'>Value</th><th class='r'>Unit</th></tr>
    <tr><td colspan='3' class='sec-lbl'>Inputs</td></tr>
    <tr><td>Hot Water IN / OUT</td><td class='r'>{fi(hot_water_in)} / {fi(hot_water_out)}</td><td class='u'>°C</td></tr>
    <tr><td>Flow Rate</td><td class='r'>{fi(flow_rate)}</td><td class='u'>Kg/Hr</td></tr>
    <tr><td>{cold_lbl}</td><td class='r'>{cold_val}</td><td class='u'>°C</td></tr>
    <tr><td>Operating Schedule</td><td class='r'>{fi(daily_op_hours)} hrs x {fi(op_days)} days</td><td class='u'></td></tr>
    <tr><td><b>Total Operating Hours</b></td><td class='r' style='color:#0063B1;font-weight:600'>{fi(daily_op_hours)} × {fi(op_days)} = {fi(daily_op_hours * op_days)}</td><td class='u'>hrs/year</td></tr>
    <tr><td>Steam Cost {fuel_info}</td><td class='r'>Rs.{ff(steam_cost)}</td><td class='u'>Rs./Kg</td></tr>
    <tr><td>Electricity Tariff</td><td class='r'>Rs.{ff(electricity_tariff)}</td><td class='u'>Rs./kWh</td></tr>
    <tr><td colspan='3' class='sec-lbl'>Fuel Savings</td></tr>
    <tr><td>Heat Duty</td><td class='r'>{fi(heat_duty_kcal)}</td><td class='u'>kCal/Hr</td></tr>
    <tr><td>Steam Required</td><td class='r'>{ff(steam_required)}</td><td class='u'>Kg/Hr</td></tr>
    <tr><td>Heating COP</td><td class='r'>{ff(cop)}</td><td class='u'></td></tr>
    <tr><td><b>Hourly Steam Savings (A)</b></td><td class='r' style='color:#0063B1;font-weight:600'>Rs.{fi(hourly_steam_savings_A)}</td><td class='u'>Rs./Hr</td></tr>
    <tr><td colspan='3' class='sec-lbl'>Electricity Operating Cost</td></tr>
    <tr><td>Electrical Power</td><td class='r'>{fi(electrical_power)}</td><td class='u'>kWhe</td></tr>
    <tr><td><b>Hourly Operating Cost (B)</b></td><td class='r' style='color:#8C3800;font-weight:600'>Rs.{fi(hourly_op_cost_B)}</td><td class='u'>Rs./Hr</td></tr>
    {"<tr><td colspan='3' class='sec-lbl'>Cooling Electricity Reduction</td></tr><tr><td>Cooling Output</td><td class='r'>" + fi(cooling_output_kw) + "</td><td class='u'>kWth</td></tr><tr><td>Hourly Cooling Savings (C)</td><td class='r' style='color:#006B6E;font-weight:600'>Rs." + fi(hourly_cooling_savings_C) + "</td><td class='u'>Rs./Hr</td></tr>" if is_hc else ""}
    <tr><td colspan='3' class='sec-lbl'>Net Savings</td></tr>
    <tr><td><b>{net_lbl}</b></td><td class='r' style='color:#6B4900;font-weight:600'>Rs.{fi(net_savings_hr)}</td><td class='u'>Rs./Hr</td></tr>
    <tr><td><b>Annual Savings</b></td><td class='r' style='color:#6B4900;font-weight:700;font-size:14px'>Rs.{fi(annual_savings)}</td><td class='u'>Rs./Year</td></tr>
    {"<tr><td colspan='3' class='sec-lbl'>CO₂ Mitigation</td></tr><tr><td>Fuel Type</td><td class='r'>" + co2_fuel + "</td><td class='u'></td></tr><tr><td>Tonnes of CO₂ Mitigated</td><td class='r' style='color:#107C10;font-weight:600'>" + ff(tonnes_co2) + "</td><td class='u'>T/yr</td></tr><tr><td>Equivalent Tree Plantation</td><td class='r' style='color:#107C10;font-weight:600'>" + fi(equivalent_trees) + "</td><td class='u'>nos.</td></tr><tr><td>Equivalent Forestation</td><td class='r' style='color:#4527A0;font-weight:600'>" + ff(equivalent_forestation) + "</td><td class='u'>ACRs</td></tr>" if has_co2 else ""}
  </table>

  <div class='footer'>
    <strong>Forbes Marshall</strong> &nbsp;|&nbsp; Heat Pump Savings Calculator &nbsp;|&nbsp; This is a reference calculator. For precise calculations, contact the authorised owner.
  </div>
</div>
</body></html>"""

    import base64
    b64     = base64.b64encode(report_body.encode()).decode()
    dl_html = (f"<a href='data:text/html;base64,{b64}' download='ForbesMarshall_HeatPump_Report.html' "
               f"style='display:inline-block;background:#118DFF;color:#FFF;font-family:Segoe UI,sans-serif;"
               f"font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;"
               f"padding:8px 20px;border-radius:2px;text-decoration:none;margin-top:12px;"
               f"box-shadow:0 1px 4px rgba(0,0,0,.15)'>Download Report (HTML)</a>")

    return kpi + dl_html, detail_html, steam_html


CSS = """
footer, .built-with, .show-api { display: none !important; }
.input-panel  { padding: 0 16px 20px !important; min-height: 100vh; }
.output-panel { padding: 16px !important; }
.pbi-divider  { border: none; border-top: 1px solid #e5e7eb; margin: 14px 0 10px; }
.pbi-sec {
  font-size: 10px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase;
  padding: 12px 0 8px; border-bottom: 1px solid #e5e7eb; margin-bottom: 10px;
  font-family: 'Segoe UI', system-ui, sans-serif;
}
"""

with gr.Blocks(title="Heat Pump Savings Calculator") as demo:

    gr.HTML("""
    <div style='background:#1B1A19;border-bottom:1px solid #323130;
                padding:0 16px;height:40px;display:flex;align-items:center;gap:10px;
                position:sticky;top:0;z-index:100'>
      <img src='data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCADhAOEDASIAAhEBAxEB/8QAHQABAAIDAQEBAQAAAAAAAAAAAAYHAQUIBAMCCf/EAEYQAAEEAgEDAQUFAgoGCwAAAAEAAgMEBREGBxIhMRMUIkFRCBUyYXEWGBckM1ViZpSl0+NCUnKBkZIjNTdzdYKxssLR8P/EABsBAQADAQEBAQAAAAAAAAAAAAABAgMEBQYH/8QAMBEAAgIBAwMCBAYBBQAAAAAAAAECEQMEITESQWETUQWBodEUInGRsfAyFWKCwfH/2gAMAwEAAhEDEQA/AKcREX6EeaEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREB0B0C6McT55wEZ7M2svFa97lh7a07Gs7W614LCd+fqrB/dl6ffzhyL+1Rf4a9H2PCB0e2ToDJWPP/Kvb1D698H4pJJTpzuz+RYdOgouBjYfo+X8I8+oHcR8wvls+fVz1M4Ym9n2OuMYKKbNV+7L0+/nDkX9qi/w0/dk6ffzhyL+1Rf4aheE+1Jfdno/vvjNSLEPeBIasz3Twt+bvPh+vppq6dqzw2q0VmvI2WGZgkje07DmkbBH5ELPUZNdpq9STV+SYrHLhFLfuy9Pv5w5F/aov8NUx9pHpvgenN7BQ4KfITNyEc7pve5WvILDGB29rW6/Gd+vyXai5G+2TyTE5jmWKw+OsCexh4pmXC3y1j5Cwhm/9YBnkfLYHrsDb4ZqtRl1CjKTa3v8AYrlhFR2KJJA9U2PqFb/2Q2Nf1lja9ocPuywdEbHqxWryXl/XSryTJ1cP03xFrGw25Y6kz6by6SIOIY4kTjZI0fQfovYza148vppLi93X/RjGFqzkvY+qBzSNhwI/VX3X5DyXm/Xfh3HOonGcVj5MfZke6pDWc3v7oTI3vDnvDhuNpA/Xa3vWLrjyfiHUnL8Yw+D446njzExj7VaR8ji6GOQk9sjQBt+ta+Sfi8jmoRhbavnarrmtx0KrbOZw5pOgRv6bTub9V031CzLeoH2Un8xzGKx0GVitN9m+rEWiMttCIlvcSQHN3sbPr+ikuc5Jyji/SLgB4Xx2lmMjeo145IJaj5j2NrBxcAxzTvYHnys/9QlX+G9tc+3mifT8nHxe0ergP1WSQPVdl9IOTdRuU8ht4vnnT+ljMSaT3if7ukhDpO5gEZEjnBwLXPOgP9FQr7KdSnB1U6gVK8UQrV5HRQM9WsY2xKGgfloD/gofxFxjNuP+NPZ3z5oenbW/JzTsfVAQfQrpyn1D6/X6EN/HdMsHZq2Y2zV5W03hskbhtrhux8wR/wAVrPtcMxg5LwiQVqlfNSMcchFF2lwb3Q9gfr1APtA3f9JaQ1snlWOUVvfEr499g4bWc7bH1CbH1C7a6xZ3qZhM1Sg4DwvHZqlJXL7Es1YvLJO4gNBErPlo+hVR9TOofWGDht6nyzgmFxGMycT6D7AqPDgZGOHwn2zgHaDiNg+ipg18s1NRW/8AuV/tQljUf/CgSQDokbWC5oGy4AfqurekBzOF+zHSzPBuOUMtyKe1KZYpYw4yatPYS74mk9sYGh3DwAvvx3nPWhuXidyfpNDLiQ13t2Y6oBY/Ce3t75y0+dbBHptJfEH1SSivytreST28UPT4+xyai3vUKzTuc5zVqhirGIrS3JHsozxCOSuSfiY5g8NIdvwPT0WiXoxfVFMzYREViAiIgCIiAIiICW8Xv89z+IZwLjL8lapOe+Z9CmO0PL/UyuGvh8D8Z7Va/Fvsu5m1j/bci5HVxlhzfgr1YDY7D8u5xc0fqBv9VYX2OYom9I3ytjY2STJT97g0Au1262fnpXQvmtb8TyY8kseJKNP9zqhiTSbP5wcjxNvAcgyGEvhotULD68vb6EtOtj8j6j8iuyfs08tx+W6PYuKzfrx2sTGadlj5QDG2MkRk7+Rj7PPp6j5LnT7UeOfjut2aLmdrbscFuP8ApNdGGE/80bx/uVYOY1x25oP6hepm061+nhbrh/QyjL05M6q66dfqVGpPx/gV1lrIP3HPk4/iirj5iI+j3/0hto/M+Byw9znvc97nPe4lznOOy4nySSfU/msNBLmtaCXOIa0AbJJ9AFI+XcK5BxPGYe7n6nuT8syWSCs/+VYxnZ5eP9Env8N9Rrzo+FtptPi0qUI8v92VlJz3ZOfsjzRQdY43zSsjZ922B3PcAN7Z9V5uonVHn9PqByKnj+YZGOnBk7EcDI5G9rWNkcGgePQAKFcE4hk+cZ/7ixL6TLPsH2CbchZGGM1vZAP1HyWz470z5Rm+dZHhVOGpFk8b3+8maUthYGODfDg0/iLm9vjyCFSePD60smRp7cPt5JTl00jZdKuVzz9cuPcl5ZmHyuFnsnuWXD4QYXxs7j6AAuaN/L1Vr9Weil/mfUPK8pxvLsBFVyJieyOZ7u5vbCyP1bsEHs3v81zhnMfYw2YvYm72GzRsSV5vZnuaXscWu7TryNg68Lf886ach4VjqGQztaiIrzuwCCXvdBJ2B/s5Rodr+129efQquXCvVjPHPpbVLZO1zsE9qasu/qPjaXAPstv4VezuOvZSW00xNrv/AJQm0JToE701u9n/AOwvl1e5Rk+PdGemuQ43mPcsjHXhjMsPY9zWmppw04EfT1Co/gnBsjyutlrWOuYbH1cUyJ9yfI2fd42iQuDPi7SPVp9deo+q9HKenmU47x6PkZyPH8pjZbfubrGJvCwGTdvf2u0Bo68/P5b9RvKOmxxmoznb6m3ty2uCzm62Rf2B51kur3TOzjcXyd/GebY+PcjY5hFFdbrWwfVrXehLfLHfVpHdHPscMdieacspZQtp2Ya0UUkczwC17ZHhw3vR8/RVJxjp7k+Rcbk5Ccnx7F4tls0xPlr4rh8wYHlrdtO/hP8A6/Qrxc34ZkOKHHjIWMTer34DPUsY+yJ4ZGg6OnaHkePl8/1T8Li6Z4ISpS7Vx3+f6dh1u1Jrgv6p046uUqcNGj1gx9arBGIoImWnhsbGjTWj4fQAALW/ars4r2vBaT8lTyGeqnV2xEW9zmD2QLn69A5wJAP9LXzVEcn4ra47jcNkMi2mYczRF+r7Jxc4RH/WBA078hv9V9eZ8XyHD82cLlPdTYEEc/8AF3lzO2Rvc3yQPOvXwrY9KvVjNzT54SV9mHPZqjr/AKu4Lm3IczTs8M6hU8BUirmOeE2S32kncT3fCD8vCqbqX066jycNv3eSdTMfmqONifdNR1h7i90bHH4Rr8WiQP1VVy9M+QR9PG86dWo/dRaHmP2n8YbGZDGJDHr8BcPXfp5Wr4RxS9y7kcODw7ajLsrJJGGdxYzTGFx8gE+gPyWeDSrFG45FUefyrtzvYlO+3PkvDpDxG1k+k9a/wnqZewebmnd77SkvNFaMh7mn/ow3ua4tDCDvz/vGp10/4v1JwvLqWT5L1VpZPEQd5s1PeC72oLHAfiAA04g7/Jcd9scrWvLWuBGxsLc5fid3FcawfIrUdT3LNic0+x23j2Lwx/eNePJ8aJ3+Svm0Tk2nNfmvmKb/AHEcldvqSDrvkMflesPJchi54rFOW00RyxEFjy2JjHEEeCO5rvPz9VCURejjh0QUF2VGTduwiIrkBERAEREAREQHZP2O/wDsfH/iVj/4q5Vxr0e65fwecP8A2e/Zb7z/AIzJP7f3/wBj+LXjt9m7019VM/3rP6hf3v8A5K+W1fw3U5M8pRjs37r7nXDLFRSbLU6zdKMN1Jp13WLUmOylQFte7HGH6afVj2EjubvzrYIPofJ3UdP7Kt33oe+c3g93B8+yxp73D6Dcmh+vlff96v8AqF/e/wDkp+9X/UL+9/8AJWmHD8Tww6ILb/iRJ4pO2Wt036O8J4NKy5QovvZNg8X7xEkrf9gaDWf+UA/mVUH24/8ArXiX/cXP/dCvV+9Z/UL+9/8AJVXdceqH8JtvET/cf3T93MmZ2+9+39p7QsO/wN1rs/P1Wmi0mrWqWXMvfe17fqROcOiomt6O5zGcf5HlLeWte7Qz4K7Vif2OduWRgDG/CCRsj19FZbOp/Eg3BZ6K6+LkOZu4n9qHexfqCKm/ue8EN895azw3ewFQCL18ukx5ZdUr/v8Ab+RiptKiwcRkuJ2uulzkObv64/HlbORa72L3GyBI58TA0DY7ndvqANb3pSrI8+4FyrjXL8NcgzGJsZiR2Xhs5CwLMbLzO0MYwRs2wOb8H0DW68fOlESWkhJptvaq+QU2ixeknLsNxfh/OYcnWoXrWRr0m06F6B8sNlzJJC8ODdaADgfJC9nUfmXHs700xGM4zTxXH2e+GzlcNXqOY42gzsE7JPwujLdDtOnDQ3v5Vcil6WDyep3u/pRHU6otnpbyLD0uATYi5zHGYuf7zdYNLL4D7xrlpjDRJHpu2vOtHZ9AfA3s6rrVluJ5MceZx2bF3L9erK3K3cdijQineXgx6jIHkAO+vr6/IV2iR00Y5PUv+Ptf1J6nVFs8m6nx1OG8NxeArYHJy0MIyveGQxLZ3QzN8dgdIPT/AGdhavrNm8DzLqrDfp5ZkeLsQVIJ7gge0QgNAkcGFu/h8nQHnXhV0iQ0sIS6o87/AFDm3sdBjqf0vm5lPVkxmbZhbGM/Z505nHuoojYa8QhnePJLgfxDuP6KveieYwXE+rde/lMs0Yqs21CLwheQ8GN7GP7AO4d2wda8b8qvkVY6OEYSgm6aodbuyU5/jXFMVg3WMX1Dp5u5H2NbUixViAybIBPc/wADQ2fP0Uvnn4VyfpTwvCX+c18FfwguixFLjZ59+2m7m6LBr0APqfVVOi0lhcquTtO729q9qITrse7P06FDLz1MZl48vUj7fZ3I4Hwtl20E6Y/4hokjz9F4URbJUiAiIpICIiAIiIAiIgJPxzgmfzuG++axxlTHGc12WL+RhrNkkABc1ve4F2gR/wDtrz8s4hm+MwUrOSZTlqXu/wB2tU7cdmGQsID2h0ZIBGx4P1/I6luOxjeU9G8NicblsJDfx2Xty2K97IxVnhkjGdrh7QjuB7T6KX8RmxfGD08wOWzuCFuCzmJLBgvxzQwCeAsi9pI0lre5xAGyuCWpnFvvu9u9JP7e3c0UUyhPVYLgGl2/A+auPh9GDi3FcHjMxl8Gbn7cY22+KtkoZzHXawtL3OY4hrdg+p8ep1sKAdUs/ks/yzKvt5A34KtuzBQA7fZRwCV3Y1gaAA3WtaXRjzepPpS29yrVI2EnTTkVfsZkL3G8bO6NshrXc7WhmY1zQ5vcwv23YIPn6r5Q9OOVuv5anar0MccRNHBdmvZCGCGOSRvcxoe52nFzdOGt+CN62FZnN4ospnpbmKwXTXkdJ9asyLJZPMMjs2g2vGwmZonjAcC0t12Dw0LHPXY/lMXOsNhs/hp7s2doXme3yEMMUkbagjeIpHFrXtY74PB3oDe/U8UdXkdXW/PjdefL5ou4Iq/LcC5Fj6lS40Y3I1rV1lCObHZGG0wWHjbI3Fjj2uI9N+PzXgHF8uKfIrE8cVY8ddG3Iwyv+NrnzexDW6BDiH+vkDXptWRx554FwrH1r2exUGRl5hTuMFHIxWXMrMiLJXuMTndrdOIO/qtlyPk+YxeU6n5N3Kakt+xDUdhLFe/DO41vvB5ayMtJ0WsLj2/iaDvx4K0/E5bpU/Pvul59yOlFFb9R8x6hbnOcazOHtY6vaq+0OTgjnoPruEzLTHnTewt33Hfjt9Qfl5CkXU/NPz/HeF5K9kY7+Xdjp2XpS9rpdttSBgk1532a1v5LcdLOXnGcE5BHblx77mBiF3jbrRBlrWZiYpTECfi+F3f26IDgHa2tpZZqCml3qvnX8+OCEldFfcmwt7jucs4TJ+wF6qQJ44ZmyiNxG+0uaSNj0I+R2PULW7HptXj0mzDIulslellrEOXfm5p7gr8grY2xI10TO1732Gu9oCQ70+e9rd18xXmz3MslQz8NbIT36bHVsVyGnV9rGysA6b3qaIe0+PYcGADuJ9fVYvWSi3Fx48/ovkT0I5z7m63sa3pZXQHMOTVcbkuW53A53Hm7a4zjPdrMVuGeV9hthrJT3AAOlABJcGg+A4ADSpTFZOiM5LkuR4yXPMmL3zRG66u6SRx33mRoJ9dnWvO1vhzyyxcun+1fj+Sso0eXDY29mMtUxWNrmxdtythgiDgO97joDZIA/U+FLIel3JbNr3Ojd41evHuDKdbPVZJ3uaCS1rA/ZPg+PyXi4BHhcl1TxTLb5MJh58h3HtvOY6tF5cG+3+Fw1oN7/B+fgqxMLUkwWZgzWD4RwKlkqznPq2H82M3snlpHcWvs9rvU+oWeozyg6j7d6+6+lkximV3iuA52/haeYdYwuOqXmufUOSysFV0zWu7S5rXuB1sEb0v27p1ykZ2LECvRe+Wg7JMtNyEJqmq06dN7bu7O0HwfO/y0QpDmMLJy7gnCnYfK4J0mNxstS5FaytevLFJ7d7gC2RzTogggjx5UlgpYGxbwuByWRxN+1iOFzxvqx5wV609p1jba8liN4BBa4ktDvkN+FSWpmu/vtXFcd/sT0orjIdP89UxN3JxW8DkK9CEz2xj8xXsPhiBAMhYxxPaCRs/mvt/BtyKOGJ2QtcexUssTZm18hm60EwY4dzS5jn7bsEHR0fqFJc5XsYXiPIfubinC8S6/jZKdqxV5V77OYHOa5zGRvndsktb6AnwpPz+R+Y5Tcy3HsF0qzFK5DXfHdyl6M2JSK8bT3h1hhbotLe3tHho+e1H4nJa3Vb77ePNd2OlFIciw+S4/nLeFy9b3a9UeGTR97XaJAcCC0kEEEEEfIrwKV9Xm4VnUnMt49LXlxwkj9m6vOZYu72TPaBjyTtof3AeSPGh4Cii7cUnKEZPukUaphERaEBERAEREAREQGND6LKIgMaH0WURAY0PoE0FlEAWNBZRAEREBjQTQ+iyiAxofRZREAWND6BZRAY0Pomh9FlEBjQ+gTQ+gWUQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQH//2Q==' style='height:28px;width:auto;object-fit:contain;border-radius:2px;margin-right:6px'>
      <span style='font-size:14px;font-weight:600;color:#F3F2F1 !important;font-family:Segoe UI,system-ui,sans-serif'>
        Heat Pump Savings Calculator
      </span>
      <div style='height:16px;width:1px;background:#3B3A39;margin:0 4px'></div>
      <span style='font-size:12px;color:#A19F9D !important;font-family:Segoe UI,system-ui,sans-serif'>
        Thermodynamic ROI Analysis
      </span>
      <div style='margin-left:auto;display:flex;align-items:center;gap:6px'>
        <div style='width:8px;height:8px;border-radius:50%;background:#107C10'></div>
        <span style='font-size:11px;color:#A19F9D !important;font-family:Segoe UI,system-ui,sans-serif'>Excel-verified</span>
      </div>
    </div>
    """)

    gr.HTML("""
    <div style='background:#FFF4CE;border-bottom:1px solid #F2C811;padding:7px 20px;
                display:flex;align-items:center;gap:8px'>
      <svg width='14' height='14' viewBox='0 0 16 16' fill='none'>
        <path d='M8 1L15 14H1L8 1Z' stroke='#8C5E00' stroke-width='1.5' fill='none'/>
        <line x1='8' y1='6' x2='8' y2='10' stroke='#8C5E00' stroke-width='1.5' stroke-linecap='round'/>
        <circle cx='8' cy='12' r='.7' fill='#8C5E00'/>
      </svg>
      <span style='font-size:11px;color:#603000;font-family:Segoe UI,system-ui,sans-serif'>
        <strong>Reference Calculator</strong> — Results are indicative only. For precise calculations and project proposals, contact the authorised owner.
      </span>
    </div>
    """)

    with gr.Row():

        with gr.Column(scale=4, min_width=280, elem_classes=["input-panel"]):
            gr.HTML("<div style='height:14px'></div>")

            gr.HTML("<div class='pbi-sec'>System Configuration</div>")
            medium       = gr.Radio(["Air", "Water"], label="Heat Pump Medium", value="Water", elem_classes=["pbi-radio"])
            gr.HTML("<div style='height:6px'></div>")
            mode         = gr.Radio(["Heating Only", "Heating + Cooling"], label="Mode", value="Heating Only", elem_classes=["pbi-radio"])
            gr.HTML("<div style='height:6px'></div>")
            process_type = gr.Radio(["Per Hour", "Per Day"], label="Process Input Type", value="Per Hour", elem_classes=["pbi-radio"])
            gr.HTML("<div style='height:6px'></div>")
            heating_type = gr.Radio(["Indirect Heating", "Direct Steam Injection"], label="Heating Method", value="Indirect Heating", elem_classes=["pbi-radio"])

            gr.HTML("<hr class='pbi-divider'><div class='pbi-sec'>Temperature &amp; Flow</div>")
            amb_temp      = gr.Number(label="Ambient Temperature (°C)  — Air source only", value=30, visible=False)
            amb_temp_info = gr.HTML(visible=False)
            gr.HTML("<div style='height:6px'></div>")
            with gr.Row():
                hot_water_in  = gr.Number(label="Hot Water IN  20–75 °C",  value=50,   min_width=100)
                hot_water_out = gr.Number(label="Hot Water OUT  25–80 °C", value=60,   min_width=100)
            gr.HTML("<div style='height:6px'></div>")
            with gr.Row():
                flow_rate     = gr.Number(label="Flow Rate (Kg/Hr or Kg/Day)", value=1000, min_width=100)
                cold_water_in = gr.Number(label="Cold Water IN  10–40 °C",     value=30,   min_width=100)
            gr.HTML("<div style='height:6px'></div>")
            cold_water_out = gr.Number(label="Cold Water OUT  7–40 °C  —  H+C only", value=25, visible=False)

            gr.HTML("<hr class='pbi-divider'><div class='pbi-sec'>Operating Schedule</div>")
            with gr.Row():
                daily_op_hours = gr.Number(label="Daily Operating Hours  (max 24)", value=22,  min_width=100)
                op_days        = gr.Number(label="Operating Days / Year  (max 360)", value=340, min_width=100)
            total_hours_display = gr.HTML(
                "<div style='font-size:12px;color:#374151;background:#F3F4F6;border-radius:4px;"
                "padding:7px 12px;margin-top:6px;font-family:Segoe UI,system-ui,sans-serif'>"
                "⏱ <b>22 hrs × 340 days = 7,480 hrs/year</b></div>"
            )

            gr.HTML("<hr class='pbi-divider'><div class='pbi-sec'>Cost Inputs</div>")
            steam_cost_known  = gr.Radio(["I know the steam cost", "Auto-calculate from fuel type"],
                                         label="Steam Cost Method", value="I know the steam cost", elem_classes=["pbi-radio"])
            gr.HTML("<div style='height:6px'></div>")
            steam_cost_manual = gr.Number(label="Steam Cost (Rs./Kg)", value=4.5, visible=True)
            fuel_type         = gr.Dropdown(list(FUEL_TABLE.keys()), label="Fuel Type (auto-calculates steam cost)", visible=False, elem_classes=["pbi-dropdown"])
            gr.HTML("<div style='height:6px'></div>")
            # shown only when user knows steam cost — for CO2 calculation
            fuel_type_co2     = gr.Dropdown(list(FUEL_TABLE.keys()), label="Fuel Type (optional — for CO₂ calculation)", visible=True, elem_classes=["pbi-dropdown"])
            gr.HTML("<div style='height:6px'></div>")
            with gr.Row():
                electricity_tariff = gr.Number(label="Electricity Tariff (Rs./kWh)", value=9,    min_width=100)
                ikw_tr             = gr.Number(label="IKW/TR  (H+C only)",            value=0.95, min_width=100, visible=False)

            gr.HTML("<div style='height:14px'></div>")
            calc_btn = gr.Button("APPLY", variant="primary")
            gr.HTML("<div style='height:10px'></div>")

        with gr.Column(scale=8, min_width=500, elem_classes=["output-panel"]):
            summary_out     = gr.HTML()
            detail_out      = gr.HTML()
            gr.HTML("<div style='height:10px'></div>")
            gr.HTML("""
            <div style='font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
                        padding:10px 0 8px;border-bottom:1px solid #e5e7eb;margin-bottom:8px;
                        font-family:Segoe UI,system-ui,sans-serif'>
              Fuel Steam Cost &amp; CO₂ Reference
            </div>""")
            steam_table_out = gr.HTML()

    # callbacks
    def upd_mode(med):
        return gr.update(visible=(med == "Water"))

    def upd_medium(med):
        is_air = (med == "Air")
        return (gr.update(visible=is_air),       # amb_temp input
                gr.update(visible=is_air),        # amb_temp_info
                gr.update(visible=not is_air))    # cold_water_in (manual, Water only)

    def upd_amb_temp(amb, med):
        if med != "Air":
            return "", gr.update()
        try:
            cw = interp_cold_water_in(float(amb))
            info = (f"<div style='font-size:12px;color:#374151;background:#F3F4F6;border-radius:4px;"
                    f"padding:7px 12px;margin-top:4px;font-family:Segoe UI,system-ui,sans-serif'>"
                    f"🌡 Ambient {float(amb):g}°C → <b>Cold Water IN auto-set to {cw}°C</b> (interpolated)</div>")
            return info, gr.update(value=cw)
        except:
            return "", gr.update()

    def upd_cooling(med, mod):
        show = (med == "Water" and mod == "Heating + Cooling")
        return gr.update(visible=show), gr.update(visible=show)

    def upd_steam(choice):
        is_manual = (choice == "I know the steam cost")
        return (gr.update(visible=is_manual),
                gr.update(visible=not is_manual),
                gr.update(visible=is_manual))

    def upd_total_hours(hrs, days):
        try:
            h = float(hrs or 0)
            d = float(days or 0)
            total = int(round(h * d))
            return (f"<div style='font-size:12px;color:#374151;background:#F3F4F6;border-radius:4px;"
                    f"padding:7px 12px;margin-top:6px;font-family:Segoe UI,system-ui,sans-serif'>"
                    f"⏱ <b>{h:g} hrs × {d:g} days = {total:,} hrs / year</b></div>")
        except:
            return ""

    medium.change(upd_medium,   [medium],              [amb_temp, amb_temp_info, cold_water_in])
    medium.change(upd_mode,     [medium],              [mode])
    medium.change(upd_cooling,  [medium, mode],        [cold_water_out, ikw_tr])
    mode.change(upd_cooling,    [medium, mode],        [cold_water_out, ikw_tr])
    amb_temp.change(upd_amb_temp, [amb_temp, medium],  [amb_temp_info, cold_water_in])
    steam_cost_known.change(upd_steam, [steam_cost_known], [steam_cost_manual, fuel_type, fuel_type_co2])
    daily_op_hours.change(upd_total_hours, [daily_op_hours, op_days], [total_hours_display])
    op_days.change(upd_total_hours,        [daily_op_hours, op_days], [total_hours_display])

    calc_btn.click(
        calculate,
        inputs=[medium, mode, process_type, heating_type,
                hot_water_in, hot_water_out, flow_rate,
                cold_water_in, cold_water_out,
                amb_temp,
                daily_op_hours, op_days,
                steam_cost_known, steam_cost_manual, fuel_type,
                fuel_type_co2,
                electricity_tariff, ikw_tr],
        outputs=[summary_out, detail_out, steam_table_out]
    )

if __name__ == "__main__":
    demo.launch(
        css=CSS,
        theme=gr.themes.Default(),
        server_name="0.0.0.0",
        server_port=10000
    )

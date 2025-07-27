rule auto_rule_20250727044136_5157 {
  strings:
    $o0 = "hWndClient" wide ascii nocase
    $o1 = "main_loop_entrance_0" wide ascii nocase
    $o2 = "differ" wide ascii nocase
    $o3 = "x7FFF" wide ascii nocase
    $o4 = "off_47900C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727044139_6580 {
  strings:
    $o0 = "word_471372" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727044143_7238 {
  condition:
    auto_rule_20250727044136_5157 or auto_rule_20250727044139_6580
}
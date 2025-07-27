rule auto_rule_20250727013243_9306 {
  strings:
    $o0 = "dword_45CAC4" wide ascii nocase
    $o1 = "main_loop_0" wide ascii nocase
    $o2 = "gu_return" wide ascii nocase
    $o3 = "tail_loop_start_0" wide ascii nocase
    $o4 = "off_45C91C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727013247_8433 {
  strings:
    $o0 = "dword_45C2D4" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727013252_7119 {
  condition:
    auto_rule_20250727013243_9306 or auto_rule_20250727013247_8433
}
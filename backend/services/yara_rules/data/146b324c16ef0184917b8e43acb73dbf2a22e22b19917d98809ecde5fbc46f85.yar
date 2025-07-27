rule auto_rule_20250727034354_3671 {
  strings:
    $o0 = "x7FFF" wide ascii nocase
    $o1 = "x45AC" wide ascii nocase
    $o2 = "x7A3F" wide ascii nocase
    $o3 = "x5688u" wide ascii nocase
    $o4 = "dword_40A718" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727034358_7968 {
  strings:
    $o0 = "x4055D7" wide ascii nocase
    $o1 = "x1B29" wide ascii nocase
    $o2 = "dword_410053" wide ascii nocase
    $o3 = "x2047u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250727034402_9083 {
  condition:
    auto_rule_20250727034354_3671 or auto_rule_20250727034358_7968
}
rule auto_rule_20250727025820_4125 {
  strings:
    $o0 = "dword_427CD4" wide ascii nocase
    $o1 = "dword_427548" wide ascii nocase
    $o2 = "__sbh_heap_init" wide ascii nocase
    $o3 = "dword_427680" wide ascii nocase
    $o4 = "UnwindUp6_0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727025821_8133 {
  strings:
    $o0 = "dword_424004" wide ascii nocase
    $o1 = "off_427518" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727025825_5409 {
  condition:
    auto_rule_20250727025820_4125 or auto_rule_20250727025821_8133
}
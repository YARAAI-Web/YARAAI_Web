rule auto_rule_20250726104809_8618 {
  strings:
    $o0 = "dword_42E891" wide ascii nocase
    $o1 = "dword_42D01C" wide ascii nocase
    $o2 = "dword_42E6ED" wide ascii nocase
    $o3 = "x58B2u" wide ascii nocase
    $o4 = "xF1E18BD7" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726104812_8914 {
  strings:
    $o0 = "x8FEC9A90" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726104816_3593 {
  condition:
    auto_rule_20250726104809_8618 or auto_rule_20250726104812_8914
}
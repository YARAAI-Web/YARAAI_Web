rule auto_rule_20250726233517_0256 {
  strings:
    $o0 = "x140u" wide ascii nocase
    $o1 = "dword_4617B0" wide ascii nocase
    $o2 = "dword_447024" wide ascii nocase
    $o3 = "UnwindUp0_0" wide ascii nocase
    $o4 = "ActiveWindow" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726233520_7978 {
  strings:
    $o0 = "phmx" wide ascii nocase
    $o1 = "CodePagea" wide ascii nocase
    $o2 = "x401891" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726233524_4088 {
  condition:
    auto_rule_20250726233517_0256 or auto_rule_20250726233520_7978
}
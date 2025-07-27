rule auto_rule_20250726153324_3471 {
  strings:
    $o0 = "dword_78028" wide ascii nocase
    $o1 = "x22C068" wide ascii nocase
    $o2 = "dword_77F74" wide ascii nocase
    $o3 = "dword_78088" wide ascii nocase
    $o4 = "xFFFEFFFF" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726153328_3157 {
  strings:
    $o0 = "dword_77FB0" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726153331_8834 {
  condition:
    auto_rule_20250726153324_3471 or auto_rule_20250726153328_3157
}
rule auto_rule_20250726164605_3643 {
  strings:
    $o0 = "dword_405584" wide ascii nocase
    $o1 = "dword_4055EC" wide ascii nocase
    $o2 = "dword_40558C" wide ascii nocase
    $o3 = "dword_410BA4" wide ascii nocase
    $o4 = "dword_40572C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726164608_8759 {
  strings:
    $o0 = "byte_407081" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726164611_7350 {
  condition:
    auto_rule_20250726164605_3643 or auto_rule_20250726164608_8759
}
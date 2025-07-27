rule auto_rule_20250726184424_7960 {
  strings:
    $o0 = "Sourcea" wide ascii nocase
    $o1 = "RtlUnwind" wide ascii nocase
    $o2 = "dword_467328" wide ascii nocase
    $o3 = "UsedDefaultChar" wide ascii nocase
    $o4 = "dword_46801C" wide ascii nocase
  condition:
    4 of ($o*)
}
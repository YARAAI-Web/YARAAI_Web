rule auto_rule_20250726192918_0108 {
  strings:
    $o0 = "hTemplateFile" wide ascii nocase
    $o1 = "uSize" wide ascii nocase
    $o2 = "dwShareMode" wide ascii nocase
    $o3 = "dword_401220" wide ascii nocase
  condition:
    4 of ($o*)
}
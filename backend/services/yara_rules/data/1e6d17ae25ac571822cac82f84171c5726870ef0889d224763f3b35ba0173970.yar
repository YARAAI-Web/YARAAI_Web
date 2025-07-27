rule auto_rule_20250726193238_6081 {
  strings:
    $o0 = "dword_47996C" wide ascii nocase
    $o1 = "differ" wide ascii nocase
    $o2 = "_getptd" wide ascii nocase
    $o3 = "DrawDibGetBuffer" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726213942_5901 {
  strings:
    $o0 = "dword_4C1288" wide ascii nocase
    $o1 = "SendKeyDownDelay" wide ascii nocase
    $o2 = "MouseCoordMode" wide ascii nocase
  condition:
    3 of ($o*)
}
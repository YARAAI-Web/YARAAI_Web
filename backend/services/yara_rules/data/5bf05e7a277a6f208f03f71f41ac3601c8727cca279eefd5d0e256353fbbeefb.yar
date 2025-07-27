rule auto_rule_20250726223616_8456 {
  strings:
    $o0 = "EnumPropsExA" wide ascii nocase
    $o1 = "hWndClient" wide ascii nocase
    $o2 = "achPath" wide ascii nocase
  condition:
    3 of ($o*)
}
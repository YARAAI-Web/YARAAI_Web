rule auto_rule_20250726071334_6211 {
  strings:
    $o0 = "yStart" wide ascii nocase
    $o1 = "GetProfileIntW" wide ascii nocase
    $o2 = "lppt" wide ascii nocase
  condition:
    3 of ($o*)
}
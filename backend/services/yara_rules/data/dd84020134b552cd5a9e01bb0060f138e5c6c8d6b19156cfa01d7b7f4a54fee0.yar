rule auto_rule_20250726084621_5383 {
  strings:
    $o0 = "off_44BBEC" wide ascii nocase
    $o1 = "__freetlocinfo" wide ascii nocase
    $o2 = "__crtInitCritSecAndSpinCount" wide ascii nocase
  condition:
    3 of ($o*)
}
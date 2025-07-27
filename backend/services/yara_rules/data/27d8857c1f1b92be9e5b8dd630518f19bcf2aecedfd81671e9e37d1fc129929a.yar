rule auto_rule_20250727001726_4803 {
  strings:
    $o0 = "_byte_0" wide ascii nocase
    $o1 = "_pLastBlock" wide ascii nocase
    $o2 = "off_464024" wide ascii nocase
  condition:
    3 of ($o*)
}
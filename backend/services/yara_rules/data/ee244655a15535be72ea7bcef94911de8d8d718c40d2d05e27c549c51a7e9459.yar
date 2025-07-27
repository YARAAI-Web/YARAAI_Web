rule auto_rule_20250726194614_1917 {
  strings:
    $o0 = "__sbh_resize_block" wide ascii nocase
    $o1 = "off_44DD0C" wide ascii nocase
    $o2 = "Runtime" wide ascii nocase
  condition:
    3 of ($o*)
}
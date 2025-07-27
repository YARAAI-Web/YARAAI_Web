rule auto_rule_20250726194313_1998 {
  strings:
    $o0 = "x12010u" wide ascii nocase
    $o1 = "off_476D28" wide ascii nocase
    $o2 = "__sbh_alloc_new_region" wide ascii nocase
  condition:
    3 of ($o*)
}
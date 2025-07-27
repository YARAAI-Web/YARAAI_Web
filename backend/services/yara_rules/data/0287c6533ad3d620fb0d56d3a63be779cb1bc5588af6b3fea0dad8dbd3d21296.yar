rule auto_rule_20250727000821_1097 {
  strings:
    $o0 = "off_10236238" wide ascii nocase
    $o1 = "xBF8000003F800000uLL" wide ascii nocase
    $o2 = "off_102361E4" wide ascii nocase
  condition:
    3 of ($o*)
}
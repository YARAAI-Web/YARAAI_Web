rule auto_rule_20250726070310_7144 {
  strings:
    $o0 = "x480u" wide ascii nocase
    $o1 = "off_48410C" wide ascii nocase
    $o2 = "_set_exp" wide ascii nocase
    $o3 = "_IsZeroMan" wide ascii nocase
  condition:
    4 of ($o*)
}
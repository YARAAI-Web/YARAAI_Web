rule auto_rule_20250726183948_9834 {
  strings:
    $o0 = "_NLG_Notify1" wide ascii nocase
    $o1 = "byte_44C581" wide ascii nocase
    $o2 = "_msize" wide ascii nocase
    $o3 = "off_44B820" wide ascii nocase
  condition:
    4 of ($o*)
}
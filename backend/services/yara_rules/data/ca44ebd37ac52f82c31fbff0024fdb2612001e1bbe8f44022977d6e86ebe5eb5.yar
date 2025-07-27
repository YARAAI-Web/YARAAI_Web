rule auto_rule_20250726183441_8576 {
  strings:
    $o0 = "off_475220" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "off_475214" wide ascii nocase
    $o3 = "_except_handler3" wide ascii nocase
  condition:
    4 of ($o*)
}
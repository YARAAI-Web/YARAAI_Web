rule auto_rule_20250726123517_2219 {
  strings:
    $o0 = "WINNLSGetEnableStatus" wide ascii nocase
    $o1 = "GetMenuContextHelpId" wide ascii nocase
    $o2 = "uMsg" wide ascii nocase
  condition:
    3 of ($o*)
}
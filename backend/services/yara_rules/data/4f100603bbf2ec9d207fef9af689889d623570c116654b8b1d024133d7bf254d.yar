rule auto_rule_20250726155139_6979 {
  strings:
    $o0 = "wsusscan" wide ascii nocase
    $o1 = "g_pProcessLocalData" wide ascii nocase
  condition:
    all of them
}
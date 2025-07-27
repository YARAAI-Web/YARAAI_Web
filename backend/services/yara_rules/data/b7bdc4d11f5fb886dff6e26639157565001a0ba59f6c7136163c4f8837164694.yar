rule auto_rule_20250727040224_0605 {
  strings:
    $o0 = "GetDialogBaseUnits" wide ascii nocase
    $o1 = "ResetWriteWatch" wide ascii nocase
  condition:
    all of them
}
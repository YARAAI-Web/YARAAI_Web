rule auto_rule_20250727042339_9126 {
  strings:
    $o0 = "ToAsciiEx" wide ascii nocase
    $o1 = "MapDialogRect" wide ascii nocase
    $o2 = "TranslateMDISysAccel" wide ascii nocase
    $o3 = "idHook" wide ascii nocase
    $o4 = "pmbi" wide ascii nocase
  condition:
    4 of ($o*)
}
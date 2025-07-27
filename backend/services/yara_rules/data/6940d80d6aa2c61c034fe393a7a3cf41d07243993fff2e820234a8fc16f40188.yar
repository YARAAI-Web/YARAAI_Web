rule auto_rule_20250726145322_5077 {
  strings:
    $o0 = "bShow" wide ascii nocase
    $o1 = "IMPQueryIMEW" wide ascii nocase
    $o2 = "lpList" wide ascii nocase
    $o3 = "SetWindowsHookA" wide ascii nocase
    $o4 = "CreateDialogParamA" wide ascii nocase
  condition:
    4 of ($o*)
}
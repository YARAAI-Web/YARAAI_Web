rule auto_rule_20250726232547_1031 {
  strings:
    $o0 = "pInputs" wide ascii nocase
    $o1 = "GetMouseMovePointsEx" wide ascii nocase
    $o2 = "IsCharUpperA" wide ascii nocase
    $o3 = "GetWindowModuleFileNameA" wide ascii nocase
    $o4 = "lpPoint" wide ascii nocase
  condition:
    4 of ($o*)
}
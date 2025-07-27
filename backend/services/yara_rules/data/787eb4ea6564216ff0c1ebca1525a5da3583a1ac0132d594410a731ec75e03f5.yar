rule auto_rule_20250726170631_9647 {
  strings:
    $o0 = "GetKeyboardLayoutNameW" wide ascii nocase
    $o1 = "ptszClassName" wide ascii nocase
    $o2 = "GetWindowRgn" wide ascii nocase
    $o3 = "GetMouseMovePointsEx" wide ascii nocase
    $o4 = "hmod" wide ascii nocase
  condition:
    4 of ($o*)
}
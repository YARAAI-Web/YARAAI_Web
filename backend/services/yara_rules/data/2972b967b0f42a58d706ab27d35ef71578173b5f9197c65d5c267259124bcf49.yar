rule auto_rule_20250726165916_9644 {
  strings:
    $o0 = "lpCreationTime" wide ascii nocase
    $o1 = "cchBufferLength" wide ascii nocase
    $o2 = "GetPriorityClass" wide ascii nocase
    $o3 = "nTabPositions" wide ascii nocase
    $o4 = "IsZoomed" wide ascii nocase
  condition:
    4 of ($o*)
}
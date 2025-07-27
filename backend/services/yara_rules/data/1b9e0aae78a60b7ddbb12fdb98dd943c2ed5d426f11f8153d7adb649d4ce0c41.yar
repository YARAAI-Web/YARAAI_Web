rule auto_rule_20250726143548_2911 {
  strings:
    $o0 = "lpBytesRead" wide ascii nocase
    $o1 = "InternalGetWindowText" wide ascii nocase
    $o2 = "lpNumberOfCharsWritten" wide ascii nocase
    $o3 = "afCmd" wide ascii nocase
    $o4 = "idTransaction" wide ascii nocase
  condition:
    4 of ($o*)
}
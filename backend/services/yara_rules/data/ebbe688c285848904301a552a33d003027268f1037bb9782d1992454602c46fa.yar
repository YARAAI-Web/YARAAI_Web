rule auto_rule_20250726234948_3163 {
  strings:
    $o0 = "__crtExitProcess" wide ascii nocase
    $o1 = "report_failure" wide ascii nocase
    $o2 = "dword_466144" wide ascii nocase
    $o3 = "dword_465D10" wide ascii nocase
    $o4 = "dword_466130" wide ascii nocase
  condition:
    4 of ($o*)
}
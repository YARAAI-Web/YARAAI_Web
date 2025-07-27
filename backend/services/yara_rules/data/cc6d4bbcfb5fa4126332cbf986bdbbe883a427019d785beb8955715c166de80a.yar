rule auto_rule_20250727025122_1040 {
  strings:
    $o0 = "dword_45FE9C" wide ascii nocase
    $o1 = "_getptd" wide ascii nocase
    $o2 = "TrailUp3" wide ascii nocase
    $o3 = "_msize" wide ascii nocase
    $o4 = "__crtInitCritSecNoSpinCount" wide ascii nocase
  condition:
    5 of ($o*)
}
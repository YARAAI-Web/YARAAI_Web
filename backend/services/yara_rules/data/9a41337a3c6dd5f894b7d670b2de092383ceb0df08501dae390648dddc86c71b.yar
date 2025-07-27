rule auto_rule_20250726215133_5201 {
  strings:
    $o0 = "word_466270" wide ascii nocase
    $o1 = "UnwindUp5_0" wide ascii nocase
    $o2 = "off_465B34" wide ascii nocase
    $o3 = "GetBrushOrgEx" wide ascii nocase
    $o4 = "InitializeCriticalSec" wide ascii nocase
  condition:
    4 of ($o*)
}
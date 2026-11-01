# 홈

**수동적 오류 허용. 글래스박스 AI. 하나의 수학적 보정.**

> QWAV는 다음의 대표 연구 이니셔티브입니다 [QNFO](https://github.com/QNFO/.github)는, 다음을 위한 지식을 발전시키는 과학 연구 인큐베이터입니다 **모든 이의 공동 이익**. QNFO는 Empowering Change(501c3)의 연구 정체성입니다. 모든 작업은 다음에 의해 관리됩니다 [QNFO 콘텐츠 라이선스 계약](https://github.com/QNFO/gitbook/blob/main/LICENSE/README.md) 및 [행동 강령](https://github.com/QNFO/gitbook/blob/main/CODE_OF_CONDUCT.md).

***

## QWAV란 무엇인가

QWAV는 양자 컴퓨팅과 인공지능을 위해 아르키메데스적(연속) 기하학을 초거리(트리 기반) 기하학으로 대체합니다. Bruhat-Tits 트리 — $p$-진수 이론에서 나온 구조 — 는 강한 삼각부등식을 통해 수동적 오류 억제를 제공하며, 4 K에서 능동적 오류 보정 없이 작동합니다.

## 주요 결과

* **깊이 7에서 논리 오류 0개** — 삼항 Bruhat-Tits 트리 인코딩, 물리적 오류율 최대 40%에서 검증됨
* **계층적 오류 격리** — 오류는 자신의 트리 가지 안에서만 전파되며, 가지를 넘어서는 일은 없음
* **글래스박스 AI** — 트리 토폴로지 위의 신경망 아키텍처로, 의사결정이 설계상 감사 가능
* **40원자 중성 원자 사양** — 입증된 실험 역량 범위 내

## 인터랙티브 데모

| #  | 산출물           | 라이브 데모                                                      | 설명                      |
| -- | ------------- | ----------------------------------------------------------- | ----------------------- |
| A1 | 오류 격리         | [데모](https://qnfo.github.io/ultrametric-error-confinement/) | Bruhat-Tits 트리 오류 시뮬레이션 |
| A2 | Q-PNA 플레이그라운드 | [데모](https://qnfo.github.io/Q-PNA/)                         | 양자-네이티브 p-진 신경 아키텍처 탐색기 |
| A3 | 수렴 탐색기        | [데모](https://qnfo.github.io/ultrametric-convergence/)       | 초거리 vs 유클리드 클러스터링       |
| A4 | 트리 거리         | [데모](https://qnfo.github.io/tree-distance/)                 | 상호작용형 공집합 거리 비교         |
| A5 | 하드웨어 시각화 도구   | [데모](https://qnfo.github.io/hardware-pathway/)              | 3D 중성 원자 트리 시각화         |
| K1 | 기술 허브         | [허브](https://qnfo.github.io/QWAV/)                          | 라이브 데모가 포함된 프로그램 개요     |

## 프로그램 관리(모두 공개)

| 기능        | 링크                                                                     |
| --------- | ---------------------------------------------------------------------- |
| **위키**    | [6개 페이지 — 아키텍처, 모듈, 출판물](https://github.com/QNFO/QWAV/wiki)            |
| **토론**    | [세션 기록, 스프린트 보고서](https://github.com/QNFO/QWAV/discussions)            |
| **칸반 보드** | [11개 이슈 — 우선순위, 스프린트, 상태](https://github.com/orgs/QNFO/projects/1)     |
| **이슈**    | [열린 3개, 닫힌 22개](https://github.com/QNFO/QWAV/issues)                   |
| **릴리스**   | [v2.73 — 스프린트 19-21](https://github.com/QNFO/QWAV/releases)            |
| **마일스톤**  | [S19(종료), S20(종료), S21(진행 중)](https://github.com/QNFO/QWAV/milestones) |
| **라벨**    | [19개 — P0-P3, 차단됨, 연구, 테스트](https://github.com/QNFO/QWAV/labels)       |

## 문서

| 문서                                                                                         | 목적                      |
| ------------------------------------------------------------------------------------------ | ----------------------- |
| [PROJECT STATE.md](https://github.com/QNFO/gitbook/blob/main/PROJECT%20STATE.md)           | LLM 인계를 위한 현재 프로그램 상태   |
| [CHANGELOG.md](https://github.com/QNFO/gitbook/blob/main/CHANGELOG.md)                     | 시간순 변경 로그(v2.74)        |
| [CHARTER.md](https://github.com/QNFO/gitbook/blob/main/CHARTER.md)                         | 프로그램 범위, 제약 조건          |
| [LEARNINGS.md](https://github.com/QNFO/gitbook/blob/main/LEARNINGS.md)                     | 29가지 교훈, 그중 1개는 차단 요인   |
| [BRAND-STRATEGY.md](https://github.com/QNFO/gitbook/blob/main/briefings/BRAND-STRATEGY.md) | QNFO/QWAV/Rowan 브랜드 정체성 |
| [이전 작업 목록](https://github.com/QNFO/gitbook/blob/main/briefings/prior-work-catalog.md)      | 30개의 외부 출판물, 7개 범주      |

## 테스트 스위트

* **102개 테스트**: 42개 구조적(unittest) + 60개 매개변수화(pytest)
* CDP 콘솔 캡처가 포함된 브라우저 스모크 테스트
* 전체 102/102 통과

## 출판물

Zenodo에 있는 40개 이상의 오픈액세스 출판물. 다음을 참조하세요 [전체 목록](https://qnfo.github.io/ultrametric-tree-universality/pub-hub.html). 주요 출판물:

* [초거리 양자 컴퓨팅의 기초](https://doi.org/10.5281/zenodo.15107688)
* [초거리 오류 격리의 검증](https://doi.org/10.5281/zenodo.15113616)
* [초거리 오류 격리의 대칭 확장](https://doi.org/10.5281/zenodo.15129661)
* [트리는 실재한다](https://doi.org/10.5281/zenodo.15241485)
* [모든 것의 바닥에 있는 트리](https://doi.org/10.5281/zenodo.15276773)

## 라이선스

**QNFO 콘텐츠 라이선스 계약 v1.1** — 다음을 참조 [LICENSE](https://github.com/QNFO/gitbook/blob/main/LICENSE/README.md) 에서 전체 약관을 확인하세요.

비상업적 사용만 허용. 출처 표기 필수. 특허 선행기술 인용 필수. 모든 QNFO 조직 및 rwnq8 개인 저장소에는 이 라이선스가 적용됩니다. 2026-05-24부터 모든 저장소에 소급 적용됩니다.

_주요 조건:_ 비독점, 양도 불가, 취소 가능. 상업적 사용은 별도 합의가 필요합니다. 무단 상업적 사용 시 85%의 손해배상액 예정. 준거법은 스위스 법, 중재는 제네바 ICC.

***

_QNFO — QWAV의 오픈소스 본거지. 모든 것을 공개합니다. 모든 것을 추적합니다._

***

## 번역

이 문서는 GitBook AI 번역을 통해 10개 이상의 언어로 제공됩니다. 상단 내비게이션 바의 언어 선택기를 사용해 언어를 전환하세요.

